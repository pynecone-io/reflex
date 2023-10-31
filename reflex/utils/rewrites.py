"""Utilities for transforming and rewriting Reflex code.

This module is used internally by Reflex to rewrite user code
where needed to better support the Reflex programming model.

Please watch out for Black Magic.
"""
from __future__ import annotations

import ast
import hashlib
import inspect
import linecache
import textwrap
from typing import Any, Callable


def replace_function_code(
    fn: Callable,
    new_source_code: str,
    locals: dict | None = None,
    filename_prefix: str = "reflex_rewrites",
) -> Callable:
    """Compile the new source code and replace the function's code object.

    The source code will be inserted into `linecache` so that stack traces,
    and other debugging tools will show the source correctly.

    Args:
        fn: The function to replace the code of.
        new_source_code: The new source code to use.
        locals: The local variables to use when compiling the new source code.
        filename_prefix: The prefix to use for the filename in `linecache`.

    Returns:
        The function with the new source code.
    """
    source_hash = hashlib.md5(new_source_code.encode()).hexdigest()
    filename = f"<{filename_prefix}_{source_hash}>"
    linecache.cache[filename] = (
        len(new_source_code),
        None,
        new_source_code.splitlines(keepends=True),
        filename,
    )
    lc = locals.copy() if locals is not None else {}
    exec(compile(new_source_code, filename, "exec"), fn.__globals__, lc)
    fn.__code__ = lc[fn.__name__].__code__
    return fn


class AddYieldAfterAsyncWithSelf(ast.NodeTransformer):
    """Transform the AST to add a `yield` statement after every `async with self:` block."""

    _REMOVE_DECORATOR = "background"

    def __init__(self):
        """Initialize the transformer."""
        super().__init__()
        self.added_yield = False
        self.self_name = None

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> Any:
        """Remove the @rx.background decorator.

        Because this transformation is applied from the @rx.background decorator, we
        need to strip it off so that it's not applied multiple times.

        Args:
            node: The node to visit.

        Returns:
            The node with the decorator removed.
        """
        # remove the background task decorator
        for dec in node.decorator_list:
            if isinstance(dec, ast.Attribute) and dec.attr == self._REMOVE_DECORATOR:
                node.decorator_list.remove(dec)
                break
            if isinstance(dec, ast.Name) and dec.id == self._REMOVE_DECORATOR:
                node.decorator_list.remove(dec)
                break
            if (
                isinstance(dec, ast.Call)
                and isinstance(dec.func, ast.Name)
                and dec.func.id == self._REMOVE_DECORATOR
            ):
                node.decorator_list.remove(dec)
                break
        for arg in node.args.args:
            self.self_name = arg.arg
            break
        self.generic_visit(node)
        return node

    def generic_visit(self, node: ast.AST) -> ast.AST:
        """Add a `yield` statement after every `async with self:` block.

        Visit all nodes with a `body` and add a `yield` statement after every
        `async with self:` block.

        Args:
            node: The node to visit.

        Returns:
            The node with the `yield` statements added, if applicable.
        """
        super().generic_visit(node)
        body: list[ast.stmt] | None = getattr(node, "body", None)
        if body is None:
            return node
        insert_yield_at = []
        for ix, child in enumerate(body):
            if (
                isinstance(child, ast.AsyncWith)
                and child.items
                and isinstance(child.items[0].context_expr, ast.Name)
                and child.items[0].context_expr.id == self.self_name
            ):
                insert_yield_at.append((ix + 1))
        for added_so_far, ix in enumerate(insert_yield_at):
            next_ix = added_so_far + ix
            if (
                next_ix < len(body)
                and isinstance(body[next_ix], ast.Expr)
                and isinstance(body[next_ix].value, ast.Yield)
            ):
                continue  # already has a yield here
            body.insert(next_ix, ast.Expr(value=ast.Yield()))
            self.added_yield = True
        return node


def add_yield_after_async_with_self(
    fn: Callable, locals: dict | None = None
) -> Callable:
    """Add a `yield` statement after every `async with self:` block.

    Rewrite the source code of `fn` to append a `yield` statement after every
    `async with self:` block.

    Args:
        fn: The function to rewrite.
        locals: The local variables to use when compiling the new source code.

    Returns:
        The function with the `yield` statements added.
    """
    orig_src = textwrap.dedent(inspect.getsource(fn))
    transformer = AddYieldAfterAsyncWithSelf()
    magic_fn_tree = transformer.visit(ast.parse(orig_src))
    if not transformer.added_yield:
        return fn  # do not rewrite the function if there were no changes
    magic_fn_source = ast.unparse(magic_fn_tree)
    return replace_function_code(fn, magic_fn_source, locals)

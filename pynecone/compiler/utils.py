"""Common utility functions used in the compiler."""

import json
import os
from typing import Dict, List, Optional, Set, Tuple, Type

from pynecone import constants
from pynecone.compiler import templates
from pynecone.components.base import (
    Body,
    ColorModeScript,
    Description,
    DocumentHead,
    Head,
    Html,
    Image,
    Link,
    Main,
    Meta,
    Script,
    Title,
)
from pynecone.components.component import Component, CustomComponent
from pynecone.event import get_hydrate_event
from pynecone.state import State
from pynecone.style import Style
from pynecone.utils import format, imports, path_ops

# To re-export this function.
merge_imports = imports.merge_imports


def compile_import_statement(lib: str, fields: Set[str]) -> str:
    """Compile an import statement.

    Args:
        lib: The library to import from.
        fields: The set of fields to import from the library.

    Returns:
        The compiled import statement.
    """
    # Check for default imports.
    defaults = {
        field
        for field in fields
        if field.lower() == lib.lower().replace("-", "").replace("/", "")
    }
    assert len(defaults) < 2

    # Get the default import, and the specific imports.
    default = next(iter(defaults), "")
    rest = fields - defaults
    return templates.format_import(lib=lib, default=default, rest=rest)


def compile_imports(imports: imports.ImportDict) -> str:
    """Compile an import dict.

    Args:
        imports: The import dict to compile.

    Returns:
        The compiled import dict.
    """
    imports = [compile_import_statement(lib, fields) for lib, fields in imports.items()]
    return templates.IMPORTS.render(imports=imports)


def compile_state(state: Type[State]) -> str:
    """Compile the state of the app.

    Args:
        state: The app state object.

    Returns:
        A string of the compiled state.
    """
    initial_state = state().dict()
    initial_state.update(
        {
            "events": [{"name": get_hydrate_event(state)}],
            "files": [],
        }
    )
    initial_state = format.format_state(initial_state)
    return initial_state

def compile_render(component: Component) -> str:
    """Compile the component's render method.

    Args:
        component: The component to compile the render method for.

    Returns:
        A string of the compiled render method.
    """
    return component.render()


def compile_custom_component(
    component: CustomComponent,
) -> Tuple[str, imports.ImportDict]:
    """Compile a custom component.

    Args:
        component: The custom component to compile.

    Returns:
        A tuple of the compiled component and the imports required by the component.
    """
    # Render the component.
    render = component.get_component()

    # Get the imports.
    imports = {
        lib: fields
        for lib, fields in render.get_imports().items()
        if lib != component.library
    }

    # Concatenate the props.
    props = ", ".join([prop.name for prop in component.get_prop_vars()])

    # Compile the component.
    return (
        templates.COMPONENT(
            name=component.tag,
            props=props,
            render=render,
        ),
        imports,
    )


def create_document_root(stylesheets: List[str]) -> Component:
    """Create the document root.

    Args:
        stylesheets: The list of stylesheets to include in the document root.

    Returns:
        The document root.
    """
    sheets = [Link.create(rel="stylesheet", href=href) for href in stylesheets]
    return Html.create(
        DocumentHead.create(*sheets),
        Body.create(
            ColorModeScript.create(),
            Main.create(),
            Script.create(),
        ),
    )


def create_theme(style: Style) -> Dict:
    """Create the base style for the app.

    Args:
        style: The style dict for the app.

    Returns:
        The base style for the app.
    """
    # Get the global style from the style dict.
    global_style = Style({k: v for k, v in style.items() if not isinstance(k, type)})

    # Root styles.
    root_style = Style({k: v for k, v in global_style.items() if k.startswith("::")})

    # Body styles.
    root_style["body"] = Style(
        {k: v for k, v in global_style.items() if k not in root_style}
    )

    # Return the theme.
    return {
        "styles": {"global": root_style},
    }


def get_page_path(path: str) -> str:
    """Get the path of the compiled JS file for the given page.

    Args:
        path: The path of the page.

    Returns:
        The path of the compiled JS file.
    """
    return os.path.join(constants.WEB_PAGES_DIR, path + constants.JS_EXT)


def get_theme_path() -> str:
    """Get the path of the base theme style.

    Returns:
        The path of the theme style.
    """
    return os.path.join(constants.WEB_UTILS_DIR, constants.THEME + constants.JS_EXT)


def get_components_path() -> str:
    """Get the path of the compiled components.

    Returns:
        The path of the compiled components.
    """
    return os.path.join(constants.WEB_UTILS_DIR, "components" + constants.JS_EXT)


def add_meta(
    page: Component, title: str, image: str, description: str, meta: List[Dict]
) -> Component:
    """Add metadata to a page.

    Args:
        page: The component for the page.
        title: The title of the page.
        image: The image for the page.
        description: The description of the page.
        meta: The metadata list.

    Returns:
        The component with the metadata added.
    """
    meta_tags = [Meta.create(**item) for item in meta]

    page.children.append(
        Head.create(
            Title.create(title),
            Description.create(content=description),
            Image.create(content=image),
            *meta_tags,
        )
    )

    return page


def write_page(path: str, code: str):
    """Write the given code to the given path.

    Args:
        path: The path to write the code to.
        code: The code to write.
    """
    path_ops.mkdir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        f.write(code)


def empty_dir(path: str, keep_files: Optional[List[str]] = None):
    """Remove all files and folders in a directory except for the keep_files.

    Args:
        path: The path to the directory that will be emptied
        keep_files: List of filenames or foldernames that will not be deleted.
    """
    # If the directory does not exist, return.
    if not os.path.exists(path):
        return

    # Remove all files and folders in the directory.
    keep_files = keep_files or []
    directory_contents = os.listdir(path)
    for element in directory_contents:
        if element not in keep_files:
            path_ops.rm(os.path.join(path, element))

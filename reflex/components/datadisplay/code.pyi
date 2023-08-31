"""Stub file for code.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Optional, Union, Dict, overload, Any
from reflex.components.libs.chakra import ChakraComponent
from reflex.components.component import Component
from reflex.vars import Var
from reflex.event import EventChain

PRISM_STYLES_PATH = "/styles/code/prism"

class CodeBlock(Component):
    @overload
    @classmethod
    def create(cls, *children, can_copy: Optional[bool] = None, copy_button: Optional[Union[bool, Component]] = None, theme: Optional[Union[Var[str], str]] = None, language: Optional[Union[Var[str], str]] = None, show_line_numbers: Optional[Union[Var[bool], bool]] = None, starting_line_number: Optional[Union[Var[int], int]] = None, wrap_long_lines: Optional[Union[Var[bool], bool]] = None, custom_style: Optional[Union[Var[Dict[str, str]], Dict[str, str]]] = None, code_tag_props: Optional[Union[Var[Dict[str, str]], Dict[str, str]]] = None, **props) -> "CodeBlock": ...  # type: ignore

class Code(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "Code": ...  # type: ignore

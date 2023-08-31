"""Stub file for tooltip.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Union, Set, overload, Optional
from reflex.components.libs.chakra import ChakraComponent
from reflex.vars import Var
from reflex.event import EventChain

class Tooltip(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, arrow_padding: Optional[Union[Var[int], int]] = None, arrow_shadow_color: Optional[Union[Var[str], str]] = None, arrow_size: Optional[Union[Var[int], int]] = None, delay: Optional[Union[Var[int], int]] = None, close_on_click: Optional[Union[Var[bool], bool]] = None, close_on_esc: Optional[Union[Var[bool], bool]] = None, close_on_mouse_down: Optional[Union[Var[bool], bool]] = None, default_is_open: Optional[Union[Var[bool], bool]] = None, direction: Optional[Union[Var[str], str]] = None, gutter: Optional[Union[Var[int], int]] = None, has_arrow: Optional[Union[Var[bool], bool]] = None, is_disabled: Optional[Union[Var[bool], bool]] = None, is_open: Optional[Union[Var[bool], bool]] = None, label: Optional[Union[Var[str], str]] = None, open_delay: Optional[Union[Var[int], int]] = None, placement: Optional[Union[Var[str], str]] = None, should_wrap_children: Optional[Union[Var[bool], bool]] = None, **props) -> "Tooltip": ...  # type: ignore

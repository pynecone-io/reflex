"""Stub file for box.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Optional, overload, Union
from reflex.components.component import Component
from reflex.components.libs.chakra import ChakraComponent
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventHandler, EventChain, EventSpec

class Box(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, element: Optional[Union[Var[str], str]] = None, src: Optional[Union[Var[str], str]] = None, alt: Optional[Union[Var[str], str]] = None, on_mouse_enter: Union[EventHandler, EventSpec] = None, on_unmount: Union[EventHandler, EventSpec] = None, on_mouse_out: Union[EventHandler, EventSpec] = None, on_mouse_up: Union[EventHandler, EventSpec] = None, on_mouse_down: Union[EventHandler, EventSpec] = None, on_mouse_leave: Union[EventHandler, EventSpec] = None, on_context_menu: Union[EventHandler, EventSpec] = None, on_mount: Union[EventHandler, EventSpec] = None, on_scroll: Union[EventHandler, EventSpec] = None, on_click: Union[EventHandler, EventSpec] = None, on_blur: Union[EventHandler, EventSpec] = None, on_mouse_over: Union[EventHandler, EventSpec] = None, on_mouse_move: Union[EventHandler, EventSpec] = None, on_focus: Union[EventHandler, EventSpec] = None, on_double_click: Union[EventHandler, EventSpec] = None, **props) -> "Box": ...  # type: ignore

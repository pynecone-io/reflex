"""Stub file for editable.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Dict, Optional, Union, overload
from reflex.components.libs.chakra import ChakraComponent
from reflex.components.component import Component
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventHandler, EventChain, EventSpec

class Editable(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, is_disabled: Optional[Union[Var[bool], bool]] = None, is_preview_focusable: Optional[Union[Var[bool], bool]] = None, placeholder: Optional[Union[Var[str], str]] = None, select_all_on_focus: Optional[Union[Var[bool], bool]] = None, start_with_edit_view: Optional[Union[Var[bool], bool]] = None, submit_on_blur: Optional[Union[Var[bool], bool]] = None, value: Optional[Union[Var[str], str]] = None, default_value: Optional[Union[Var[str], str]] = None, on_blur: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_cancel: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_change: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_context_menu: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_double_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_edit: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_focus: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_scroll: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_submit: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_unmount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "Editable":  # type: ignore
        """Create the component.

        Args:
            *children: The children of the component.
            is_disabled: If true, the Editable will be disabled.
            is_preview_focusable: If true, the read only view, has a tabIndex set to 0 so it can receive focus via the keyboard or click.
            placeholder: The placeholder text when the value is empty.
            select_all_on_focus: If true, the input's text will be highlighted on focus.
            start_with_edit_view: If true, the Editable will start with edit mode by default.
            submit_on_blur: If true, it'll update the value onBlur and turn off the edit mode.
            value: The value of the Editable in both edit & preview mode
            default_value: The initial value of the Editable in both edit and preview mode.
            **props: The props of the component.

        Returns:
            The component.

        Raises:
            TypeError: If an invalid child is passed.
        """
        ...

class EditableInput(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, on_blur: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_context_menu: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_double_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_focus: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_scroll: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_unmount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "EditableInput":  # type: ignore
        """Create the component.

        Args:
            *children: The children of the component.
            **props: The props of the component.

        Returns:
            The component.

        Raises:
            TypeError: If an invalid child is passed.
        """
        ...

class EditableTextarea(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, on_blur: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_context_menu: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_double_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_focus: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_scroll: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_unmount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "EditableTextarea":  # type: ignore
        """Create the component.

        Args:
            *children: The children of the component.
            **props: The props of the component.

        Returns:
            The component.

        Raises:
            TypeError: If an invalid child is passed.
        """
        ...

class EditablePreview(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, on_blur: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_context_menu: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_double_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_focus: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_scroll: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_unmount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "EditablePreview":  # type: ignore
        """Create the component.

        Args:
            *children: The children of the component.
            **props: The props of the component.

        Returns:
            The component.

        Raises:
            TypeError: If an invalid child is passed.
        """
        ...

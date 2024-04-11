"""Stub file for reflex/components/chakra/forms/select.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Any, Dict, List, Union
from reflex.components.chakra import ChakraComponent, LiteralInputVariant
from reflex.components.chakra.typography.text import Text
from reflex.components.component import Component
from reflex.components.core.foreach import Foreach
from reflex.constants import EventTriggers
from reflex.utils.types import _issubclass
from reflex.vars import Var

class Select(ChakraComponent):
    def get_event_triggers(self) -> Dict[str, Union[Var, Any]]: ...
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        value: Optional[Union[Var[str], str]] = None,
        default_value: Optional[Union[Var[str], str]] = None,
        placeholder: Optional[Union[Var[str], str]] = None,
        error_border_color: Optional[Union[Var[str], str]] = None,
        focus_border_color: Optional[Union[Var[str], str]] = None,
        is_disabled: Optional[Union[Var[bool], bool]] = None,
        is_invalid: Optional[Union[Var[bool], bool]] = None,
        is_required: Optional[Union[Var[bool], bool]] = None,
        variant: Optional[
            Union[
                Var[Literal["outline", "filled", "flushed", "unstyled"]],
                Literal["outline", "filled", "flushed", "unstyled"],
            ]
        ] = None,
        size: Optional[Union[Var[str], str]] = None,
        name: Optional[Union[Var[str], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_change: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_paste: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "Select":
        """Create a select component.

        If a list is provided as the first children, a default component
        will be created for each item in the list.

        Args:
            *children: The children of the component.
            value: State var to bind the select.
            default_value: The default value of the select.
            placeholder: The placeholder text.
            error_border_color: The border color when the select is invalid.
            focus_border_color: The border color when the select is focused.
            is_disabled: If true, the select will be disabled.
            is_invalid: If true, the form control will be invalid. This has 2 side effects: - The FormLabel and FormErrorIcon will have `data-invalid` set to true - The form element (e.g, Input) will have `aria-invalid` set to true
            is_required: If true, the form control will be required. This has 2 side effects: - The FormLabel will show a required indicator - The form element (e.g, Input) will have `aria-required` set to true
            variant: "outline" | "filled" | "flushed" | "unstyled"
            size: The size of the select.
            name: The name of the form field
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.
        """
        ...

class Option(Text):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        value: Optional[Union[Var[Any], Any]] = None,
        as_: Optional[Union[Var[str], str]] = None,
        no_of_lines: Optional[Union[Var[int], int]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_paste: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "Option":
        """Create a select option component.

        By default, the value of the option is the text of the option.

        Args:
            *children: The children of the component.
            as_: Override the tag. The default tag is `<p>`.
            no_of_lines: Truncate text after a specific number of lines. It will render an ellipsis when the text exceeds the width of the viewport or max_width prop.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.
        """
        ...

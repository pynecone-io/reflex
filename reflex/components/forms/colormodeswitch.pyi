"""Stub file for reflex/components/forms/colormodeswitch.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Any
from reflex.components.component import BaseComponent, Component
from reflex.components.layout.cond import Cond, cond
from reflex.components.media.icon import Icon
from reflex.style import color_mode, toggle_color_mode
from reflex.vars import Var
from .button import Button
from .switch import Switch

DEFAULT_COLOR_MODE: str
DEFAULT_LIGHT_ICON: Icon
DEFAULT_DARK_ICON: Icon

def color_mode_cond(light: Any, dark: Any = None) -> Var | Component: ...

class ColorModeIcon(Cond):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        cond: Optional[Union[Var[Any], Any]] = None,
        comp1: Optional[BaseComponent] = None,
        comp2: Optional[BaseComponent] = None,
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
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "ColorModeIcon":
        """Create an icon component based on color_mode.

        Args:
            light_component: the component to display when color mode is default
            dark_component: the component to display when color mode is dark (non-default)

        Returns:
            The conditionally rendered component
        """
        ...

class ColorModeSwitch(Switch):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        is_checked: Optional[Union[Var[bool], bool]] = None,
        is_disabled: Optional[Union[Var[bool], bool]] = None,
        is_focusable: Optional[Union[Var[bool], bool]] = None,
        is_invalid: Optional[Union[Var[bool], bool]] = None,
        is_read_only: Optional[Union[Var[bool], bool]] = None,
        is_required: Optional[Union[Var[bool], bool]] = None,
        name: Optional[Union[Var[str], str]] = None,
        value: Optional[Union[Var[str], str]] = None,
        spacing: Optional[Union[Var[str], str]] = None,
        placeholder: Optional[Union[Var[str], str]] = None,
        color_scheme: Optional[
            Union[
                Var[
                    Literal[
                        "none",
                        "gray",
                        "red",
                        "orange",
                        "yellow",
                        "green",
                        "teal",
                        "blue",
                        "cyan",
                        "purple",
                        "pink",
                        "whiteAlpha",
                        "blackAlpha",
                        "linkedin",
                        "facebook",
                        "messenger",
                        "whatsapp",
                        "twitter",
                        "telegram",
                    ]
                ],
                Literal[
                    "none",
                    "gray",
                    "red",
                    "orange",
                    "yellow",
                    "green",
                    "teal",
                    "blue",
                    "cyan",
                    "purple",
                    "pink",
                    "whiteAlpha",
                    "blackAlpha",
                    "linkedin",
                    "facebook",
                    "messenger",
                    "whatsapp",
                    "twitter",
                    "telegram",
                ],
            ]
        ] = None,
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
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "ColorModeSwitch":
        """Create a switch component bound to color_mode.

        Args:
            *children: The children of the component.
            is_checked: If true, the switch will be checked. You'll need to set an on_change event handler to update its value (since it is now controlled)
            is_disabled: If true, the switch will be disabled
            is_focusable: If true and is_disabled prop is set, the switch will remain tabbable but not interactive.
            is_invalid: If true, the switch is marked as invalid. Changes style of unchecked state.
            is_read_only: If true, the switch will be readonly
            is_required: If true, the switch will be required
            name: The name of the input field in a switch (Useful for form submission).
            value: The value of the input field when checked (use is_checked prop for a bool)
            spacing: The spacing between the switch and its label text (0.5rem)
            placeholder: The placeholder text.
            color_scheme: The color scheme of the switch (e.g. "blue", "green", "red", etc.)
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props to pass to the component.

        Returns:
            The switch component.
        """
        ...

class ColorModeButton(Button):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        icon_spacing: Optional[Union[Var[int], int]] = None,
        is_active: Optional[Union[Var[bool], bool]] = None,
        is_disabled: Optional[Union[Var[bool], bool]] = None,
        is_full_width: Optional[Union[Var[bool], bool]] = None,
        is_loading: Optional[Union[Var[bool], bool]] = None,
        loading_text: Optional[Union[Var[str], str]] = None,
        size: Optional[
            Union[Var[Literal["sm", "md", "lg", "xs"]], Literal["sm", "md", "lg", "xs"]]
        ] = None,
        variant: Optional[
            Union[
                Var[Literal["ghost", "outline", "solid", "link", "unstyled"]],
                Literal["ghost", "outline", "solid", "link", "unstyled"],
            ]
        ] = None,
        color_scheme: Optional[
            Union[
                Var[
                    Literal[
                        "none",
                        "gray",
                        "red",
                        "orange",
                        "yellow",
                        "green",
                        "teal",
                        "blue",
                        "cyan",
                        "purple",
                        "pink",
                        "whiteAlpha",
                        "blackAlpha",
                        "linkedin",
                        "facebook",
                        "messenger",
                        "whatsapp",
                        "twitter",
                        "telegram",
                    ]
                ],
                Literal[
                    "none",
                    "gray",
                    "red",
                    "orange",
                    "yellow",
                    "green",
                    "teal",
                    "blue",
                    "cyan",
                    "purple",
                    "pink",
                    "whiteAlpha",
                    "blackAlpha",
                    "linkedin",
                    "facebook",
                    "messenger",
                    "whatsapp",
                    "twitter",
                    "telegram",
                ],
            ]
        ] = None,
        spinner_placement: Optional[
            Union[Var[Literal["start", "end"]], Literal["start", "end"]]
        ] = None,
        type_: Optional[Union[Var[str], str]] = None,
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
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "ColorModeButton":
        """Create a button component that calls toggle_color_mode on click.

        Args:
            *children: The children of the component.
            icon_spacing: The space between the button icon and label.
            is_active: If true, the button will be styled in its active state.
            is_disabled: If true, the button will be styled in its disabled state.
            is_full_width: If true, the button will take up the full width of its container.
            is_loading: If true, the button will show a spinner.
            loading_text: The label to show in the button when isLoading is true If no text is passed, it only shows the spinner.
            size: "lg" | "md" | "sm" | "xs"
            variant: "ghost" | "outline" | "solid" | "link" | "unstyled"
            color_scheme: Built in color scheme for ease of use.  Options:  "whiteAlpha" | "blackAlpha" | "gray" | "red" | "orange" | "yellow" | "green" | "teal" | "blue" | "cyan"  | "purple" | "pink" | "linkedin" | "facebook" | "messenger" | "whatsapp" | "twitter" | "telegram"
            spinner_placement: Position of the loading spinner.  Options:  "start" | "end"
            type_: The type of button.
            name: The name of the form field
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props to pass to the component.

        Returns:
            The switch component.
        """
        ...

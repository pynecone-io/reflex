"""Stub file for reflex/components/radix/themes/components/segmented_control.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from types import SimpleNamespace
from typing import Any, Callable, Dict, List, Literal, Optional, Union, overload

from reflex.components.core.breakpoints import Breakpoints
from reflex.event import EventHandler, EventSpec
from reflex.ivars.base import ImmutableVar
from reflex.style import Style

from ..base import RadixThemesComponent

class SegmentedControlRoot(RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        size: Optional[
            Union[
                ImmutableVar[
                    Union[
                        Breakpoints[str, Literal["1", "2", "3"]], Literal["1", "2", "3"]
                    ]
                ],
                Literal["1", "2", "3"],
                Breakpoints[str, Literal["1", "2", "3"]],
            ]
        ] = None,
        variant: Optional[
            Union[
                ImmutableVar[Literal["classic", "surface"]],
                Literal["classic", "surface"],
            ]
        ] = None,
        type: Optional[
            Union[
                ImmutableVar[Literal["single", "multiple"]],
                Literal["single", "multiple"],
            ]
        ] = None,
        color_scheme: Optional[
            Union[
                ImmutableVar[
                    Literal[
                        "tomato",
                        "red",
                        "ruby",
                        "crimson",
                        "pink",
                        "plum",
                        "purple",
                        "violet",
                        "iris",
                        "indigo",
                        "blue",
                        "cyan",
                        "teal",
                        "jade",
                        "green",
                        "grass",
                        "brown",
                        "orange",
                        "sky",
                        "mint",
                        "lime",
                        "yellow",
                        "amber",
                        "gold",
                        "bronze",
                        "gray",
                    ]
                ],
                Literal[
                    "tomato",
                    "red",
                    "ruby",
                    "crimson",
                    "pink",
                    "plum",
                    "purple",
                    "violet",
                    "iris",
                    "indigo",
                    "blue",
                    "cyan",
                    "teal",
                    "jade",
                    "green",
                    "grass",
                    "brown",
                    "orange",
                    "sky",
                    "mint",
                    "lime",
                    "yellow",
                    "amber",
                    "gold",
                    "bronze",
                    "gray",
                ],
            ]
        ] = None,
        radius: Optional[
            Union[
                ImmutableVar[Literal["none", "small", "medium", "large", "full"]],
                Literal["none", "small", "medium", "large", "full"],
            ]
        ] = None,
        default_value: Optional[
            Union[ImmutableVar[Union[List[str], str]], str, List[str]]
        ] = None,
        value: Optional[
            Union[ImmutableVar[Union[List[str], str]], str, List[str]]
        ] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[ImmutableVar, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_change: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        **props,
    ) -> "SegmentedControlRoot":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            size: The size of the segmented control: "1" | "2" | "3"
            variant: Variant of button: "classic" | "surface"
            color_scheme: Override theme color for button
            radius: The radius of the segmented control: "none" | "small" | "medium" | "large" | "full"
            default_value: The default value of the segmented control.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Component properties.

        Returns:
            A new component instance.
        """
        ...

class SegmentedControlItem(RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        value: Optional[Union[ImmutableVar[str], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[ImmutableVar, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        **props,
    ) -> "SegmentedControlItem":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            value: The value of the item.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Component properties.

        Returns:
            A new component instance.
        """
        ...

class SegmentedControl(SimpleNamespace):
    root = staticmethod(SegmentedControlRoot.create)
    item = staticmethod(SegmentedControlItem.create)

segmented_control = SegmentedControl()

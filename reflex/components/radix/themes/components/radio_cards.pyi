"""Stub file for reflex/components/radix/themes/components/radio_cards.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from types import SimpleNamespace
from typing import Any, Callable, Dict, Literal, Optional, Union, overload

from reflex.components.core.breakpoints import Breakpoints
from reflex.event import EventHandler, EventSpec
from reflex.ivars.base import ImmutableVar
from reflex.style import Style
from reflex.vars import Var

from ..base import RadixThemesComponent

class RadioCardsRoot(RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        as_child: Optional[Union[Var[bool], bool]] = None,
        size: Optional[
            Union[
                Var[
                    Union[
                        Breakpoints[str, Literal["1", "2", "3"]], Literal["1", "2", "3"]
                    ]
                ],
                Literal["1", "2", "3"],
                Breakpoints[str, Literal["1", "2", "3"]],
            ]
        ] = None,
        variant: Optional[
            Union[Var[Literal["classic", "surface"]], Literal["classic", "surface"]]
        ] = None,
        color_scheme: Optional[
            Union[
                Var[
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
        high_contrast: Optional[Union[Var[bool], bool]] = None,
        columns: Optional[
            Union[
                Var[
                    Union[
                        Breakpoints[
                            str,
                            Union[
                                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                                str,
                            ],
                        ],
                        Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                        str,
                    ]
                ],
                str,
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                Breakpoints[
                    str,
                    Union[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"], str],
                ],
            ]
        ] = None,
        gap: Optional[
            Union[
                Var[
                    Union[
                        Breakpoints[
                            str,
                            Union[
                                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                                str,
                            ],
                        ],
                        Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                        str,
                    ]
                ],
                str,
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                Breakpoints[
                    str,
                    Union[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"], str],
                ],
            ]
        ] = None,
        default_value: Optional[Union[Var[str], str]] = None,
        value: Optional[Union[Var[str], str]] = None,
        name: Optional[Union[Var[str], str]] = None,
        disabled: Optional[Union[Var[bool], bool]] = None,
        required: Optional[Union[Var[bool], bool]] = None,
        orientation: Optional[
            Union[
                Var[Literal["horizontal", "vertical", "undefined"]],
                Literal["horizontal", "vertical", "undefined"],
            ]
        ] = None,
        dir: Optional[Union[Var[Literal["ltr", "rtl"]], Literal["ltr", "rtl"]]] = None,
        loop: Optional[Union[Var[bool], bool]] = None,
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
        on_value_change: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        **props,
    ) -> "RadioCardsRoot":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            as_child: Change the default rendered element for the one passed as a child, merging their props and behavior.
            size: The size of the checkbox cards: "1" | "2" | "3"
            variant: Variant of button: "classic" | "surface" | "soft"
            color_scheme: Override theme color for button
            high_contrast: Uses a higher contrast color for the component.
            columns: The number of columns:
            gap: The gap between the checkbox cards:
            value: The controlled value of the radio item to check. Should be used in conjunction with onValueChange.
            name: The name of the group. Submitted with its owning form as part of a name/value pair.
            disabled: When true, prevents the user from interacting with radio items.
            required: When true, indicates that the user must check a radio item before the owning form can be submitted.
            orientation: The orientation of the component.
            dir: The reading direction of the radio group. If omitted,  inherits globally from DirectionProvider or assumes LTR (left-to-right) reading mode.
            loop: When true, keyboard navigation will loop from last item to first, and vice versa.
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

class RadioCardsItem(RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        as_child: Optional[Union[Var[bool], bool]] = None,
        value: Optional[Union[Var[str], str]] = None,
        disabled: Optional[Union[Var[bool], bool]] = None,
        required: Optional[Union[Var[bool], bool]] = None,
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
    ) -> "RadioCardsItem":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            as_child: Change the default rendered element for the one passed as a child, merging their props and behavior.
            value: The value given as data when submitted with a name.
            disabled: When true, prevents the user from interacting with the radio item.
            required: When true, indicates that the user must check the radio item before the owning form can be submitted.
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

class RadioCards(SimpleNamespace):
    root = staticmethod(RadioCardsRoot.create)
    item = staticmethod(RadioCardsItem.create)

radio_cards = RadioCards()

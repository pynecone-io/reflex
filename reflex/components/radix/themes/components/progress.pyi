"""Stub file for reflex/components/radix/themes/components/progress.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Dict, Literal, Optional, Union, overload

from reflex.components.core.breakpoints import Breakpoints
from reflex.event import BASE_STATE, EventType
from reflex.style import Style
from reflex.vars.base import Var

from ..base import RadixThemesComponent

class Progress(RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        value: Optional[Union[Var[int], int]] = None,
        max: Optional[Union[Var[int], int]] = None,
        size: Optional[
            Union[
                Breakpoints[str, Literal["1", "2", "3"]],
                Literal["1", "2", "3"],
                Var[
                    Union[
                        Breakpoints[str, Literal["1", "2", "3"]], Literal["1", "2", "3"]
                    ]
                ],
            ]
        ] = None,
        variant: Optional[
            Union[
                Literal["classic", "soft", "surface"],
                Var[Literal["classic", "soft", "surface"]],
            ]
        ] = None,
        color_scheme: Optional[
            Union[
                Literal[
                    "amber",
                    "blue",
                    "bronze",
                    "brown",
                    "crimson",
                    "cyan",
                    "gold",
                    "grass",
                    "gray",
                    "green",
                    "indigo",
                    "iris",
                    "jade",
                    "lime",
                    "mint",
                    "orange",
                    "pink",
                    "plum",
                    "purple",
                    "red",
                    "ruby",
                    "sky",
                    "teal",
                    "tomato",
                    "violet",
                    "yellow",
                ],
                Var[
                    Literal[
                        "amber",
                        "blue",
                        "bronze",
                        "brown",
                        "crimson",
                        "cyan",
                        "gold",
                        "grass",
                        "gray",
                        "green",
                        "indigo",
                        "iris",
                        "jade",
                        "lime",
                        "mint",
                        "orange",
                        "pink",
                        "plum",
                        "purple",
                        "red",
                        "ruby",
                        "sky",
                        "teal",
                        "tomato",
                        "violet",
                        "yellow",
                    ]
                ],
            ]
        ] = None,
        high_contrast: Optional[Union[Var[bool], bool]] = None,
        radius: Optional[
            Union[
                Literal["full", "large", "medium", "none", "small"],
                Var[Literal["full", "large", "medium", "none", "small"]],
            ]
        ] = None,
        duration: Optional[Union[Var[str], str]] = None,
        fill_color: Optional[Union[Var[str], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[EventType[[], BASE_STATE]] = None,
        on_click: Optional[EventType[[], BASE_STATE]] = None,
        on_context_menu: Optional[EventType[[], BASE_STATE]] = None,
        on_double_click: Optional[EventType[[], BASE_STATE]] = None,
        on_focus: Optional[EventType[[], BASE_STATE]] = None,
        on_mount: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_down: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_enter: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_leave: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_move: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_out: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_over: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_up: Optional[EventType[[], BASE_STATE]] = None,
        on_scroll: Optional[EventType[[], BASE_STATE]] = None,
        on_unmount: Optional[EventType[[], BASE_STATE]] = None,
        **props,
    ) -> "Progress":
        """Create a Progress component.

        Args:
            *children: The children of the component.
            value: The value of the progress bar: 0 to max (default 100)
            max: The maximum progress value.
            size: The size of the progress bar: "1" | "2" | "3"
            variant: The variant of the progress bar: "classic" | "surface" | "soft"
            color_scheme: The color theme of the progress bar
            high_contrast: Whether to render the progress bar with higher contrast color against background
            radius: Override theme radius for progress bar: "none" | "small" | "medium" | "large" | "full"
            duration: The duration of the progress bar animation. Once the duration times out, the progress bar will start an indeterminate animation.
            fill_color: The color of the progress bar fill animation.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Returns:
            The Progress Component.
        """
        ...

progress = Progress.create

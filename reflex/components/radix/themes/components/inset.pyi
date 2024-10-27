"""Stub file for reflex/components/radix/themes/components/inset.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Dict, Literal, Optional, Union, overload

from reflex.components.core.breakpoints import Breakpoints
from reflex.components.el import elements
from reflex.event import EventType
from reflex.style import Style
from reflex.vars.base import Var

from ..base import RadixThemesComponent

LiteralButtonSize = Literal["1", "2", "3", "4"]

class Inset(elements.Div, RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        side: Optional[
            Union[
                Breakpoints[str, Literal["bottom", "left", "right", "top", "x", "y"]],
                Literal["bottom", "left", "right", "top", "x", "y"],
                Var[
                    Union[
                        Breakpoints[
                            str, Literal["bottom", "left", "right", "top", "x", "y"]
                        ],
                        Literal["bottom", "left", "right", "top", "x", "y"],
                    ]
                ],
            ]
        ] = None,
        clip: Optional[
            Union[
                Breakpoints[str, Literal["border-box", "padding-box"]],
                Literal["border-box", "padding-box"],
                Var[
                    Union[
                        Breakpoints[str, Literal["border-box", "padding-box"]],
                        Literal["border-box", "padding-box"],
                    ]
                ],
            ]
        ] = None,
        p: Optional[
            Union[
                Breakpoints[str, Union[int, str]],
                Var[Union[Breakpoints[str, Union[int, str]], int, str]],
                int,
                str,
            ]
        ] = None,
        px: Optional[
            Union[
                Breakpoints[str, Union[int, str]],
                Var[Union[Breakpoints[str, Union[int, str]], int, str]],
                int,
                str,
            ]
        ] = None,
        py: Optional[
            Union[
                Breakpoints[str, Union[int, str]],
                Var[Union[Breakpoints[str, Union[int, str]], int, str]],
                int,
                str,
            ]
        ] = None,
        pt: Optional[
            Union[
                Breakpoints[str, Union[int, str]],
                Var[Union[Breakpoints[str, Union[int, str]], int, str]],
                int,
                str,
            ]
        ] = None,
        pr: Optional[
            Union[
                Breakpoints[str, Union[int, str]],
                Var[Union[Breakpoints[str, Union[int, str]], int, str]],
                int,
                str,
            ]
        ] = None,
        pb: Optional[
            Union[
                Breakpoints[str, Union[int, str]],
                Var[Union[Breakpoints[str, Union[int, str]], int, str]],
                int,
                str,
            ]
        ] = None,
        pl: Optional[
            Union[
                Breakpoints[str, Union[int, str]],
                Var[Union[Breakpoints[str, Union[int, str]], int, str]],
                int,
                str,
            ]
        ] = None,
        access_key: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        auto_capitalize: Optional[
            Union[Var[Union[bool, int, str]], bool, int, str]
        ] = None,
        content_editable: Optional[
            Union[Var[Union[bool, int, str]], bool, int, str]
        ] = None,
        context_menu: Optional[
            Union[Var[Union[bool, int, str]], bool, int, str]
        ] = None,
        dir: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        draggable: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        enter_key_hint: Optional[
            Union[Var[Union[bool, int, str]], bool, int, str]
        ] = None,
        hidden: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        input_mode: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        item_prop: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        lang: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        role: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        slot: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        spell_check: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        tab_index: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        title: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[EventType[[]]] = None,
        on_click: Optional[EventType[[]]] = None,
        on_context_menu: Optional[EventType[[]]] = None,
        on_double_click: Optional[EventType[[]]] = None,
        on_focus: Optional[EventType[[]]] = None,
        on_mount: Optional[EventType[[]]] = None,
        on_mouse_down: Optional[EventType[[]]] = None,
        on_mouse_enter: Optional[EventType[[]]] = None,
        on_mouse_leave: Optional[EventType[[]]] = None,
        on_mouse_move: Optional[EventType[[]]] = None,
        on_mouse_out: Optional[EventType[[]]] = None,
        on_mouse_over: Optional[EventType[[]]] = None,
        on_mouse_up: Optional[EventType[[]]] = None,
        on_scroll: Optional[EventType[[]]] = None,
        on_unmount: Optional[EventType[[]]] = None,
        **props,
    ) -> "Inset":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            side: The side
            clip: How to clip the element's content: "border-box" | "padding-box"
            p: Padding
            px: Padding on the x axis
            py: Padding on the y axis
            pt: Padding on the top
            pr: Padding on the right
            pb: Padding on the bottom
            pl: Padding on the left
            access_key:  Provides a hint for generating a keyboard shortcut for the current element.
            auto_capitalize: Controls whether and how text input is automatically capitalized as it is entered/edited by the user.
            content_editable: Indicates whether the element's content is editable.
            context_menu: Defines the ID of a <menu> element which will serve as the element's context menu.
            dir: Defines the text direction. Allowed values are ltr (Left-To-Right) or rtl (Right-To-Left)
            draggable: Defines whether the element can be dragged.
            enter_key_hint: Hints what media types the media element is able to play.
            hidden: Defines whether the element is hidden.
            input_mode: Defines the type of the element.
            item_prop: Defines the name of the element for metadata purposes.
            lang: Defines the language used in the element.
            role: Defines the role of the element.
            slot: Assigns a slot in a shadow DOM shadow tree to an element.
            spell_check: Defines whether the element may be checked for spelling errors.
            tab_index: Defines the position of the current element in the tabbing order.
            title: Defines a tooltip for the element.
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

inset = Inset.create

"""Stub file for reflex/components/radix/themes/components/popover.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Dict, Literal, Optional, Union, overload

from reflex.components.component import ComponentNamespace
from reflex.components.core.breakpoints import Breakpoints
from reflex.components.el import elements
from reflex.event import EventType
from reflex.style import Style
from reflex.vars.base import Var

from ..base import RadixThemesComponent, RadixThemesTriggerComponent

class PopoverRoot(RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        open: Optional[Union[Var[bool], bool]] = None,
        modal: Optional[Union[Var[bool], bool]] = None,
        default_open: Optional[Union[Var[bool], bool]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, Any]]] = None,
        on_blur: Optional[EventType[()]] = None,
        on_click: Optional[EventType[()]] = None,
        on_context_menu: Optional[EventType[()]] = None,
        on_double_click: Optional[EventType[()]] = None,
        on_focus: Optional[EventType[()]] = None,
        on_mount: Optional[EventType[()]] = None,
        on_mouse_down: Optional[EventType[()]] = None,
        on_mouse_enter: Optional[EventType[()]] = None,
        on_mouse_leave: Optional[EventType[()]] = None,
        on_mouse_move: Optional[EventType[()]] = None,
        on_mouse_out: Optional[EventType[()]] = None,
        on_mouse_over: Optional[EventType[()]] = None,
        on_mouse_up: Optional[EventType[()]] = None,
        on_open_change: Optional[Union[EventType[()], EventType[bool]]] = None,
        on_scroll: Optional[EventType[()]] = None,
        on_unmount: Optional[EventType[()]] = None,
        **props,
    ) -> "PopoverRoot":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            open: The controlled open state of the popover.
            modal: The modality of the popover. When set to true, interaction with outside elements will be disabled and only popover content will be visible to screen readers.
            on_open_change: Fired when the open state changes.
            default_open: The open state of the popover when it is initially rendered. Use when you do not need to control its open state.
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

class PopoverTrigger(RadixThemesTriggerComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, Any]]] = None,
        on_blur: Optional[EventType[()]] = None,
        on_click: Optional[EventType[()]] = None,
        on_context_menu: Optional[EventType[()]] = None,
        on_double_click: Optional[EventType[()]] = None,
        on_focus: Optional[EventType[()]] = None,
        on_mount: Optional[EventType[()]] = None,
        on_mouse_down: Optional[EventType[()]] = None,
        on_mouse_enter: Optional[EventType[()]] = None,
        on_mouse_leave: Optional[EventType[()]] = None,
        on_mouse_move: Optional[EventType[()]] = None,
        on_mouse_out: Optional[EventType[()]] = None,
        on_mouse_over: Optional[EventType[()]] = None,
        on_mouse_up: Optional[EventType[()]] = None,
        on_scroll: Optional[EventType[()]] = None,
        on_unmount: Optional[EventType[()]] = None,
        **props,
    ) -> "PopoverTrigger":
        """Create a new RadixThemesTriggerComponent instance.

        Args:
            children: The children of the component.
            props: The properties of the component.

        Returns:
            The new RadixThemesTriggerComponent instance.
        """
        ...

class PopoverContent(elements.Div, RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        size: Optional[
            Union[
                Breakpoints[str, Literal["1", "2", "3", "4"]],
                Literal["1", "2", "3", "4"],
                Var[
                    Union[
                        Breakpoints[str, Literal["1", "2", "3", "4"]],
                        Literal["1", "2", "3", "4"],
                    ]
                ],
            ]
        ] = None,
        side: Optional[
            Union[
                Literal["bottom", "left", "right", "top"],
                Var[Literal["bottom", "left", "right", "top"]],
            ]
        ] = None,
        side_offset: Optional[Union[Var[int], int]] = None,
        align: Optional[
            Union[
                Literal["center", "end", "start"],
                Var[Literal["center", "end", "start"]],
            ]
        ] = None,
        align_offset: Optional[Union[Var[int], int]] = None,
        avoid_collisions: Optional[Union[Var[bool], bool]] = None,
        collision_padding: Optional[
            Union[
                Dict[str, Union[float, int]],
                Var[Union[Dict[str, Union[float, int]], float, int]],
                float,
                int,
            ]
        ] = None,
        sticky: Optional[
            Union[Literal["always", "partial"], Var[Literal["always", "partial"]]]
        ] = None,
        hide_when_detached: Optional[Union[Var[bool], bool]] = None,
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
        custom_attrs: Optional[Dict[str, Union[Var, Any]]] = None,
        on_blur: Optional[EventType[()]] = None,
        on_click: Optional[EventType[()]] = None,
        on_close_auto_focus: Optional[EventType[()]] = None,
        on_context_menu: Optional[EventType[()]] = None,
        on_double_click: Optional[EventType[()]] = None,
        on_escape_key_down: Optional[EventType[()]] = None,
        on_focus: Optional[EventType[()]] = None,
        on_focus_outside: Optional[EventType[()]] = None,
        on_interact_outside: Optional[EventType[()]] = None,
        on_mount: Optional[EventType[()]] = None,
        on_mouse_down: Optional[EventType[()]] = None,
        on_mouse_enter: Optional[EventType[()]] = None,
        on_mouse_leave: Optional[EventType[()]] = None,
        on_mouse_move: Optional[EventType[()]] = None,
        on_mouse_out: Optional[EventType[()]] = None,
        on_mouse_over: Optional[EventType[()]] = None,
        on_mouse_up: Optional[EventType[()]] = None,
        on_open_auto_focus: Optional[EventType[()]] = None,
        on_pointer_down_outside: Optional[EventType[()]] = None,
        on_scroll: Optional[EventType[()]] = None,
        on_unmount: Optional[EventType[()]] = None,
        **props,
    ) -> "PopoverContent":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            size: Size of the button: "1" | "2" | "3" | "4"
            side: The preferred side of the anchor to render against when open. Will be reversed when collisions occur and avoidCollisions is enabled.
            side_offset: The distance in pixels from the anchor.
            align: The preferred alignment against the anchor. May change when collisions occur.
            align_offset: The vertical distance in pixels from the anchor.
            avoid_collisions: When true, overrides the side andalign preferences to prevent collisions with boundary edges.
            collision_padding: The distance in pixels from the boundary edges where collision detection should occur. Accepts a number (same for all sides), or a partial padding object, for example: { "top": 20, "left": 20 }. Defaults to 0.
            sticky: The sticky behavior on the align axis. "partial" will keep the content in the boundary as long as the trigger is at least partially in the boundary whilst "always" will keep the content in the boundary regardless. Defaults to "partial".
            hide_when_detached: Whether to hide the content when the trigger becomes fully occluded. Defaults to False.
            on_open_auto_focus: Fired when the dialog is opened.
            on_close_auto_focus: Fired when the dialog is closed.
            on_escape_key_down: Fired when the escape key is pressed.
            on_pointer_down_outside: Fired when the pointer is down outside the dialog.
            on_focus_outside: Fired when focus moves outside the dialog.
            on_interact_outside: Fired when the pointer interacts outside the dialog.
            access_key: Provides a hint for generating a keyboard shortcut for the current element.
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

class PopoverClose(RadixThemesTriggerComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, Any]]] = None,
        on_blur: Optional[EventType[()]] = None,
        on_click: Optional[EventType[()]] = None,
        on_context_menu: Optional[EventType[()]] = None,
        on_double_click: Optional[EventType[()]] = None,
        on_focus: Optional[EventType[()]] = None,
        on_mount: Optional[EventType[()]] = None,
        on_mouse_down: Optional[EventType[()]] = None,
        on_mouse_enter: Optional[EventType[()]] = None,
        on_mouse_leave: Optional[EventType[()]] = None,
        on_mouse_move: Optional[EventType[()]] = None,
        on_mouse_out: Optional[EventType[()]] = None,
        on_mouse_over: Optional[EventType[()]] = None,
        on_mouse_up: Optional[EventType[()]] = None,
        on_scroll: Optional[EventType[()]] = None,
        on_unmount: Optional[EventType[()]] = None,
        **props,
    ) -> "PopoverClose":
        """Create a new RadixThemesTriggerComponent instance.

        Args:
            children: The children of the component.
            props: The properties of the component.

        Returns:
            The new RadixThemesTriggerComponent instance.
        """
        ...

class Popover(ComponentNamespace):
    root = staticmethod(PopoverRoot.create)
    trigger = staticmethod(PopoverTrigger.create)
    content = staticmethod(PopoverContent.create)
    close = staticmethod(PopoverClose.create)

popover = Popover()

"""Stub file for reflex/components/radix/themes/components/tooltip.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Any, Dict, Literal, Union
from reflex.components.component import Component
from reflex.constants import EventTriggers
from reflex.utils import format
from reflex.vars import Var
from ..base import RadixThemesComponent

LiteralSideType = Literal["top", "right", "bottom", "left"]
LiteralAlignType = Literal["start", "center", "end"]
LiteralStickyType = Literal["partial", "always"]

class Tooltip(RadixThemesComponent):
    def get_event_triggers(self) -> Dict[str, Any]: ...
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        content: Optional[Union[Var[str], str]] = None,
        default_open: Optional[Union[Var[bool], bool]] = None,
        open: Optional[Union[Var[bool], bool]] = None,
        side: Optional[
            Union[
                Var[Literal["top", "right", "bottom", "left"]],
                Literal["top", "right", "bottom", "left"],
            ]
        ] = None,
        side_offset: Optional[Union[Var[Union[float, int]], Union[float, int]]] = None,
        align: Optional[
            Union[
                Var[Literal["start", "center", "end"]],
                Literal["start", "center", "end"],
            ]
        ] = None,
        align_offset: Optional[Union[Var[Union[float, int]], Union[float, int]]] = None,
        avoid_collisions: Optional[Union[Var[bool], bool]] = None,
        collision_padding: Optional[
            Union[
                Var[Union[float, int, Dict[str, Union[float, int]]]],
                Union[float, int, Dict[str, Union[float, int]]],
            ]
        ] = None,
        arrow_padding: Optional[
            Union[Var[Union[float, int]], Union[float, int]]
        ] = None,
        sticky: Optional[
            Union[Var[Literal["partial", "always"]], Literal["partial", "always"]]
        ] = None,
        hide_when_detached: Optional[Union[Var[bool], bool]] = None,
        delay_duration: Optional[
            Union[Var[Union[float, int]], Union[float, int]]
        ] = None,
        disable_hoverable_content: Optional[Union[Var[bool], bool]] = None,
        force_mount: Optional[Union[Var[bool], bool]] = None,
        aria_label: Optional[Union[Var[str], str]] = None,
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
        on_escape_key_down: Optional[
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
        on_open_change: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_pointer_down_outside: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "Tooltip":
        """Initialize the Tooltip component.

        Run some additional handling on the props.

        Args:
            *children: The positional arguments
            content: The content of the tooltip.
            default_open: The open state of the tooltip when it is initially rendered. Use when you do not need to control its open state.
            open: The controlled open state of the tooltip. Must be used in conjunction with `on_open_change`.
            side: The preferred side of the trigger to render against when open. Will be reversed when collisions occur and `avoid_collisions` is enabled.The position of the tooltip. Defaults to "top".
            side_offset: The distance in pixels from the trigger. Defaults to 0.
            align: The preferred alignment against the trigger. May change when collisions occur. Defaults to "center".
            align_offset: An offset in pixels from the "start" or "end" alignment options.
            avoid_collisions: When true, overrides the side and align preferences to prevent collisions with boundary edges. Defaults to True.
            collision_padding: The distance in pixels from the boundary edges where collision detection should occur. Accepts a number (same for all sides), or a partial padding object, for example: { "top": 20, "left": 20 }. Defaults to 0.
            arrow_padding: The padding between the arrow and the edges of the content. If your content has border-radius, this will prevent it from overflowing the corners. Defaults to 0.
            sticky: The sticky behavior on the align axis. "partial" will keep the content in the boundary as long as the trigger is at least partially in the boundary whilst "always" will keep the content in the boundary regardless. Defaults to "partial".
            hide_when_detached: Whether to hide the content when the trigger becomes fully occluded. Defaults to False.
            delay_duration: Override the duration in milliseconds to customize the open delay for a specific tooltip. Default is 700.
            disable_hoverable_content: Prevents Tooltip content from remaining open when hovering.
            force_mount: Used to force mounting when more control is needed. Useful when controlling animation with React animation libraries.
            aria_label: By default, screenreaders will announce the content inside the component. If this is not descriptive enough, or you have content that cannot be announced, use aria-label as a more descriptive label.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The keyword arguments

        Returns:
            The created component.
        """
        ...

tooltip = Tooltip.create

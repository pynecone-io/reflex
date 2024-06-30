"""Stub file for reflex/components/react_player/react_player.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Callable, Dict, Optional, Union, overload

from reflex.components.component import NoSSRComponent
from reflex.event import EventHandler, EventSpec
from reflex.style import Style
from reflex.vars import BaseVar, Var

class ReactPlayer(NoSSRComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        url: Optional[Union[Var[str], str]] = None,
        playing: Optional[Union[Var[bool], bool]] = None,
        loop: Optional[Union[Var[bool], bool]] = None,
        controls: Optional[Union[Var[bool], bool]] = None,
        light: Optional[Union[Var[bool], bool]] = None,
        volume: Optional[Union[Var[float], float]] = None,
        muted: Optional[Union[Var[bool], bool]] = None,
        width: Optional[Union[Var[str], str]] = None,
        height: Optional[Union[Var[str], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_buffer: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_buffer_end: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_click_preview: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_disable_pip: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_duration: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_enable_pip: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_ended: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_error: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_pause: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_play: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_playback_quality_change: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_playback_rate_change: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_progress: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_ready: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_seek: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_start: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        **props,
    ) -> "ReactPlayer":
        """Create the component.

        Args:
            *children: The children of the component.
            url: The url of a video or song to play
            playing: Set to true or false to pause or play the media
            loop: Set to true or false to loop the media
            controls: Set to true or false to display native player controls.
            light: Set to true to show just the video thumbnail, which loads the full player on click
            volume: Set the volume of the player, between 0 and 1
            muted: Mutes the player
            width: Set the width of the player: ex:640px
            height: Set the height of the player: ex:640px
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

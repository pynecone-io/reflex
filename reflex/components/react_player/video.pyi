"""Stub file for reflex/components/react_player/video.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Dict, Optional, Union, overload

import reflex
from reflex.components.react_player.react_player import ReactPlayer
from reflex.event import EventType
from reflex.style import Style
from reflex.vars.base import Var

class Video(ReactPlayer):
    pass

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
        on_blur: Optional[EventType[[]]] = None,
        on_buffer: Optional[EventType[[]]] = None,
        on_buffer_end: Optional[EventType[[]]] = None,
        on_click: Optional[EventType[[]]] = None,
        on_click_preview: Optional[EventType[[]]] = None,
        on_context_menu: Optional[EventType[[]]] = None,
        on_disable_pip: Optional[EventType[[]]] = None,
        on_double_click: Optional[EventType[[]]] = None,
        on_duration: Optional[EventType[float]] = None,
        on_enable_pip: Optional[EventType[[]]] = None,
        on_ended: Optional[EventType[[]]] = None,
        on_error: Optional[EventType[[]]] = None,
        on_focus: Optional[EventType[[]]] = None,
        on_mount: Optional[EventType[[]]] = None,
        on_mouse_down: Optional[EventType[[]]] = None,
        on_mouse_enter: Optional[EventType[[]]] = None,
        on_mouse_leave: Optional[EventType[[]]] = None,
        on_mouse_move: Optional[EventType[[]]] = None,
        on_mouse_out: Optional[EventType[[]]] = None,
        on_mouse_over: Optional[EventType[[]]] = None,
        on_mouse_up: Optional[EventType[[]]] = None,
        on_pause: Optional[EventType[[]]] = None,
        on_play: Optional[EventType[[]]] = None,
        on_playback_quality_change: Optional[EventType[[]]] = None,
        on_playback_rate_change: Optional[EventType[[]]] = None,
        on_progress: Optional[
            EventType[reflex.components.react_player.react_player.Progress]
        ] = None,
        on_ready: Optional[EventType[[]]] = None,
        on_scroll: Optional[EventType[[]]] = None,
        on_seek: Optional[EventType[float]] = None,
        on_start: Optional[EventType[[]]] = None,
        on_unmount: Optional[EventType[[]]] = None,
        **props,
    ) -> "Video":
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
            on_ready: Called when media is loaded and ready to play. If playing is set to true, media will play immediately.
            on_start: Called when media starts playing.
            on_play: Called when media starts or resumes playing after pausing or buffering.
            on_progress: Callback containing played and loaded progress as a fraction, and playedSeconds and loadedSeconds in seconds. eg { played: 0.12, playedSeconds: 11.3, loaded: 0.34, loadedSeconds: 16.7 }
            on_duration: Callback containing duration of the media, in seconds.
            on_pause: Called when media is paused.
            on_buffer: Called when media starts buffering.
            on_buffer_end: Called when media has finished buffering. Works for files, YouTube and Facebook.
            on_seek: Called when media seeks with seconds parameter.
            on_playback_rate_change: Called when playback rate of the player changed. Only supported by YouTube, Vimeo (if enabled), Wistia, and file paths.
            on_playback_quality_change: Called when playback quality of the player changed. Only supported by YouTube (if enabled).
            on_ended: Called when media finishes playing. Does not fire when loop is set to true.
            on_error: Called when an error occurs whilst attempting to play media.
            on_click_preview: Called when user clicks the light mode preview.
            on_enable_pip: Called when picture-in-picture mode is enabled.
            on_disable_pip: Called when picture-in-picture mode is disabled.
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

"""Stub file for reflex/components/next/image.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Dict, Literal, Optional, Union, overload

from reflex.event import BASE_STATE, EventType
from reflex.style import Style
from reflex.vars.base import Var

from .base import NextComponent

class Image(NextComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        width: Optional[Union[int, str]] = None,
        height: Optional[Union[int, str]] = None,
        src: Optional[Union[Any, Var[Any]]] = None,
        alt: Optional[Union[Var[str], str]] = None,
        loader: Optional[Union[Any, Var[Any]]] = None,
        fill: Optional[Union[Var[bool], bool]] = None,
        sizes: Optional[Union[Var[str], str]] = None,
        quality: Optional[Union[Var[int], int]] = None,
        priority: Optional[Union[Var[bool], bool]] = None,
        placeholder: Optional[Union[Var[str], str]] = None,
        loading: Optional[
            Union[Literal["eager", "lazy"], Var[Literal["eager", "lazy"]]]
        ] = None,
        blurDataURL: Optional[Union[Var[str], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, Any]]] = None,
        on_blur: Optional[EventType[[], BASE_STATE]] = None,
        on_click: Optional[EventType[[], BASE_STATE]] = None,
        on_context_menu: Optional[EventType[[], BASE_STATE]] = None,
        on_double_click: Optional[EventType[[], BASE_STATE]] = None,
        on_error: Optional[EventType[[], BASE_STATE]] = None,
        on_focus: Optional[EventType[[], BASE_STATE]] = None,
        on_load: Optional[EventType[[], BASE_STATE]] = None,
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
    ) -> "Image":
        """Create an Image component from next/image.

        Args:
            *children: The children of the component.
            width: The width of the image.
            height: The height of the image.
            src: This can be either an absolute external URL, or an internal path
            alt: Used to describe the image for screen readers and search engines.
            loader: A custom function used to resolve image URLs.
            fill: A boolean that causes the image to fill the parent element, which is useful when the width and height are unknown. Default to True
            sizes: A string, similar to a media query, that provides information about how wide the image will be at different breakpoints.
            quality: The quality of the optimized image, an integer between 1 and 100, where 100 is the best quality and therefore largest file size. Defaults to 75.
            priority: When true, the image will be considered high priority and preload. Lazy loading is automatically disabled for images using priority.
            placeholder: A placeholder to use while the image is loading. Possible values are blur, empty, or data:image/.... Defaults to empty.
            loading: Allows passing CSS styles to the underlying image element.  style: Var[Any]  The loading behavior of the image. Defaults to lazy. Can hurt performance, recommended to use `priority` instead.
            blurDataURL: A Data URL to be used as a placeholder image before the src image successfully loads. Only takes effect when combined with placeholder="blur".
            on_load: Fires when the image has loaded.
            on_error: Fires when the image has an error.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props:The props of the component.

        Returns:
            _type_: _description_
        """
        ...

"""Stub file for reflex/components/radix/themes/components/skeleton.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Callable, Dict, Optional, Union, overload

from reflex.components.core.breakpoints import Breakpoints
from reflex.event import EventHandler, EventSpec
from reflex.style import Style
from reflex.vars.base import Var

from ..base import RadixLoadingProp, RadixThemesComponent

class Skeleton(RadixLoadingProp, RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        width: Optional[
            Union[Breakpoints[str, str], Var[Union[Breakpoints[str, str], str]], str]
        ] = None,
        min_width: Optional[
            Union[Breakpoints[str, str], Var[Union[Breakpoints[str, str], str]], str]
        ] = None,
        max_width: Optional[
            Union[Breakpoints[str, str], Var[Union[Breakpoints[str, str], str]], str]
        ] = None,
        height: Optional[
            Union[Breakpoints[str, str], Var[Union[Breakpoints[str, str], str]], str]
        ] = None,
        min_height: Optional[
            Union[Breakpoints[str, str], Var[Union[Breakpoints[str, str], str]], str]
        ] = None,
        max_height: Optional[
            Union[Breakpoints[str, str], Var[Union[Breakpoints[str, str], str]], str]
        ] = None,
        loading: Optional[Union[Var[bool], bool]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[Union[EventHandler, EventSpec, list, Callable, Var]] = None,
        on_click: Optional[Union[EventHandler, EventSpec, list, Callable, Var]] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_focus: Optional[Union[EventHandler, EventSpec, list, Callable, Var]] = None,
        on_mount: Optional[Union[EventHandler, EventSpec, list, Callable, Var]] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        **props,
    ) -> "Skeleton":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            width: The width of the skeleton
            min_width: The minimum width of the skeleton
            max_width: The maximum width of the skeleton
            height: The height of the skeleton
            min_height: The minimum height of the skeleton
            max_height: The maximum height of the skeleton
            loading: If set, show an rx.spinner instead of the component children.
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

skeleton = Skeleton.create

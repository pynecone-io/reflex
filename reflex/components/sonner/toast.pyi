"""Stub file for reflex/components/sonner/toast.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Literal, Optional
from reflex.base import Base
from reflex.components.component import Component, ComponentNamespace
from reflex.components.lucide.icon import Icon
from reflex.event import EventSpec, call_script
from reflex.style import color_mode
from reflex.utils import format
from reflex.utils.imports import ImportVar
from reflex.utils.serializers import serialize
from reflex.vars import Var, VarData

LiteralPosition = Literal[
    "top-left",
    "top-center",
    "top-right",
    "bottom-left",
    "bottom-center",
    "bottom-right",
]
toast_ref = Var.create_safe("refs['__toast']")

class PropsBase(Base):
    def json(self) -> str: ...

class ToastProps(PropsBase):
    description: str
    close_button: bool
    invert: bool
    important: bool
    duration: int
    position: LiteralPosition
    dismissible: bool
    icon: Optional[Icon]
    action: str
    cancel: str
    id: str
    unstyled: bool
    action_button_styles: dict[str, str]
    cancel_button_styles: dict[str, str]

class Toaster(Component):
    @staticmethod
    def send_toast(message: str, level: str | None = None, **props) -> EventSpec: ...
    @staticmethod
    def toast_info(message: str, **kwargs): ...
    @staticmethod
    def toast_warning(message: str, **kwargs): ...
    @staticmethod
    def toast_error(message: str, **kwargs): ...
    @staticmethod
    def toast_success(message: str, **kwargs): ...
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        theme: Optional[Union[Var[str], str]] = None,
        rich_colors: Optional[Union[Var[bool], bool]] = None,
        expand: Optional[Union[Var[bool], bool]] = None,
        visibleToasts: Optional[Union[Var[int], int]] = None,
        position: Optional[
            Union[
                Var[
                    Literal[
                        "top-left",
                        "top-center",
                        "top-right",
                        "bottom-left",
                        "bottom-center",
                        "bottom-right",
                    ]
                ],
                Literal[
                    "top-left",
                    "top-center",
                    "top-right",
                    "bottom-left",
                    "bottom-center",
                    "bottom-right",
                ],
            ]
        ] = None,
        close_button: Optional[Union[Var[bool], bool]] = None,
        offset: Optional[Union[Var[str], str]] = None,
        dir: Optional[Union[Var[str], str]] = None,
        hotkey: Optional[Union[Var[str], str]] = None,
        invert: Optional[Union[Var[bool], bool]] = None,
        toast_options: Optional[Union[Var[ToastProps], ToastProps]] = None,
        gap: Optional[Union[Var[int], int]] = None,
        loadingIcon: Optional[Union[Var[Icon], Icon]] = None,
        pause_when_page_is_hidden: Optional[Union[Var[bool], bool]] = None,
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
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "Toaster":
        """Create the component.

        Args:
            *children: The children of the component.
            theme: the theme of the toast
            rich_colors: whether to show rich colors
            expand: whether to expand the toast
            visibleToasts: the number of toasts that are currently visible
            position: the position of the toast
            close_button: whether to show the close button
            offset: offset of the toast
            dir: directionality of the toast (default: ltr)
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

class ToastNamespace(ComponentNamespace):
    provider = staticmethod(Toaster.create)
    options = staticmethod(ToastProps)
    info = staticmethod(Toaster.toast_info)
    warning = staticmethod(Toaster.toast_warning)
    error = staticmethod(Toaster.toast_error)
    success = staticmethod(Toaster.toast_success)

    @staticmethod
    def __call__(message: str, level: str | None, **props) -> "Optional[EventSpec]":
        """Send a toast message.

        Args:
            message: The message to display.
            level: The level of the toast.
            **props: The options for the toast.

        Returns:
            The toast event.
        """
        ...

toast = ToastNamespace()

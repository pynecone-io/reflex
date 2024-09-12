"""Stub file for reflex/components/core/banner.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Callable, Dict, Literal, Optional, Union, overload

from reflex.components.component import Component
from reflex.components.el.elements.typography import Div
from reflex.components.lucide.icon import Icon
from reflex.components.sonner.toast import Toaster, ToastProps
from reflex.constants.compiler import CompileVars
from reflex.event import EventHandler, EventSpec
from reflex.style import Style
from reflex.utils.imports import ImportVar
from reflex.vars import VarData
from reflex.vars.base import Var
from reflex.vars.number import BooleanVar

connect_error_var_data: VarData
connect_errors = Var.create(
    value=CompileVars.CONNECT_ERROR, _var_data=connect_error_var_data
)
connection_error = Var.create(
    value="((connectErrors.length > 0) ? connectErrors[connectErrors.length - 1].message : '')",
    _var_data=connect_error_var_data,
)
connection_errors_count = Var.create(
    value="connectErrors.length", _var_data=connect_error_var_data
)
has_connection_errors = Var.create(
    value="(connectErrors.length > 0)", _var_data=connect_error_var_data
).to(BooleanVar)
has_too_many_connection_errors = Var.create(
    value="(connectErrors.length >= 2)", _var_data=connect_error_var_data
).to(BooleanVar)

class WebsocketTargetURL(Var):
    @classmethod
    def create(cls) -> Var: ...  # type: ignore

def default_connection_error() -> list[str | Var | Component]: ...

class ConnectionToaster(Toaster):
    def add_hooks(self) -> list[str | Var]: ...
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        theme: Optional[Union[Var[str], str]] = None,
        rich_colors: Optional[Union[Var[bool], bool]] = None,
        expand: Optional[Union[Var[bool], bool]] = None,
        visible_toasts: Optional[Union[Var[int], int]] = None,
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
        loading_icon: Optional[Union[Var[Icon], Icon]] = None,
        pause_when_page_is_hidden: Optional[Union[Var[bool], bool]] = None,
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
        on_scroll: Optional[Union[EventHandler, EventSpec, list, Callable, Var]] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        **props,
    ) -> "ConnectionToaster":
        """Create a connection toaster component.

        Args:
            *children: The children of the component.
            theme: the theme of the toast
            rich_colors: whether to show rich colors
            expand: whether to expand the toast
            visible_toasts: the number of toasts that are currently visible
            position: the position of the toast
            close_button: whether to show the close button
            offset: offset of the toast
            dir: directionality of the toast (default: ltr)
            hotkey: Keyboard shortcut that will move focus to the toaster area.
            invert: Dark toasts in light mode and vice versa.
            toast_options: These will act as default options for all toasts. See toast() for all available options.
            gap: Gap between toasts when expanded
            loading_icon: Changes the default loading icon
            pause_when_page_is_hidden: Pauses toast timers when the page is hidden, e.g., when the tab is backgrounded, the browser is minimized, or the OS is locked.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Returns:
            The connection toaster component.
        """
        ...

class ConnectionBanner(Component):
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
        on_scroll: Optional[Union[EventHandler, EventSpec, list, Callable, Var]] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        **props,
    ) -> "ConnectionBanner":
        """Create a connection banner component.

        Args:
            comp: The component to render when there's a server connection error.

        Returns:
            The connection banner component.
        """
        ...

class ConnectionModal(Component):
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
        on_scroll: Optional[Union[EventHandler, EventSpec, list, Callable, Var]] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        **props,
    ) -> "ConnectionModal":
        """Create a connection banner component.

        Args:
            comp: The component to render when there's a server connection error.

        Returns:
            The connection banner component.
        """
        ...

class WifiOffPulse(Icon):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        size: Optional[Union[Var[int], int]] = None,
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
        on_scroll: Optional[Union[EventHandler, EventSpec, list, Callable, Var]] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        **props,
    ) -> "WifiOffPulse":
        """Create a wifi_off icon with an animated opacity pulse.

        Args:
            *children: The children of the component.
            size: The size of the icon in pixels.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Returns:
            The icon component with default props applied.
        """
        ...

    def add_imports(self) -> dict[str, str | ImportVar | list[str | ImportVar]]: ...

class ConnectionPulser(Div):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        access_key: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        auto_capitalize: Optional[
            Union[Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        content_editable: Optional[
            Union[Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        context_menu: Optional[
            Union[Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        dir: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        draggable: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        enter_key_hint: Optional[
            Union[Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        hidden: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        input_mode: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        item_prop: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        lang: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        role: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        slot: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        spell_check: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        tab_index: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        title: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
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
        on_scroll: Optional[Union[EventHandler, EventSpec, list, Callable, Var]] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        **props,
    ) -> "ConnectionPulser":
        """Create a connection pulser component.

        Args:
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
            **props: The properties of the component.

        Returns:
            The connection pulser component.
        """
        ...

connection_banner = ConnectionBanner.create
connection_modal = ConnectionModal.create
connection_toaster = ConnectionToaster.create
connection_pulser = ConnectionPulser.create

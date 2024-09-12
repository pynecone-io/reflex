"""Stub file for reflex/components/el/elements/base.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Callable, Dict, Optional, Union, overload

from reflex.components.el.element import Element
from reflex.event import EventHandler, EventSpec
from reflex.style import Style
from reflex.vars.base import Var

class BaseHTML(Element):
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
    ) -> "BaseHTML":
        """Create the component.

        Args:
            *children: The children of the component.
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
            **props: The props of the component.

        Returns:
            The component.
        """
        ...

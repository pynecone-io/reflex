"""Stub file for reflex/components/el/elements/metadata.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Callable, Dict, Optional, Union, overload

from reflex.components.el.element import Element
from reflex.event import EventHandler, EventSpec
from reflex.style import Style
from reflex.vars import Var

from .base import BaseHTML

class Base(BaseHTML):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        href: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        target: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
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
    ) -> "Base":
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

class Head(BaseHTML):
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
    ) -> "Head":
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

class Link(BaseHTML):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        cross_origin: Optional[
            Union[Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        href: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        href_lang: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        integrity: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        media: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        referrer_policy: Optional[
            Union[Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        rel: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        sizes: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        type: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
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
    ) -> "Link":
        """Create the component.

        Args:
            *children: The children of the component.
            cross_origin: Specifies the CORS settings for the linked resource
            href: Specifies the URL of the linked document/resource
            href_lang: Specifies the language of the text in the linked document
            integrity: Allows a browser to check the fetched link for integrity
            media: Specifies on what device the linked document will be displayed
            referrer_policy: Specifies the referrer policy of the linked document
            rel: Specifies the relationship between the current document and the linked one
            sizes: Specifies the sizes of icons for visual media
            type: Specifies the MIME type of the linked document
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

class Meta(BaseHTML):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        char_set: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        content: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        http_equiv: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        name: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
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
    ) -> "Meta":
        """Create the component.

        Args:
            *children: The children of the component.
            char_set: Specifies the character encoding for the HTML document
            content: Defines the content of the metadata
            http_equiv: Provides an HTTP header for the information/value of the content attribute
            name: Specifies a name for the metadata
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

class Title(Element):
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
    ) -> "Title":
        """Create the component.

        Args:
            *children: The children of the component.
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

class StyleEl(Element):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        media: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
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
    ) -> "StyleEl":
        """Create the component.

        Args:
            *children: The children of the component.
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

base = Base.create
head = Head.create
link = Link.create
meta = Meta.create
title = Title.create
style = StyleEl.create

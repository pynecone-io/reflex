"""Stub file for reflex/components/radix/themes/layout/list.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Dict, Iterable, Literal, Optional, Union, overload

from reflex.components.component import Component, ComponentNamespace
from reflex.components.el.elements.typography import Li, Ol, Ul
from reflex.event import BASE_STATE, EventType
from reflex.style import Style
from reflex.vars.base import Var

LiteralListStyleTypeUnordered = Literal["none", "disc", "circle", "square"]
LiteralListStyleTypeOrdered = Literal[
    "none",
    "decimal",
    "decimal-leading-zero",
    "lower-roman",
    "upper-roman",
    "lower-greek",
    "lower-latin",
    "upper-latin",
    "armenian",
    "georgian",
    "lower-alpha",
    "upper-alpha",
    "hiragana",
    "katakana",
]

class BaseList(Component):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        list_style_type: Optional[
            Union[
                Literal[
                    "armenian",
                    "decimal",
                    "decimal-leading-zero",
                    "georgian",
                    "hiragana",
                    "katakana",
                    "lower-alpha",
                    "lower-greek",
                    "lower-latin",
                    "lower-roman",
                    "none",
                    "upper-alpha",
                    "upper-latin",
                    "upper-roman",
                ],
                Literal["circle", "disc", "none", "square"],
                Var[
                    Union[
                        Literal[
                            "armenian",
                            "decimal",
                            "decimal-leading-zero",
                            "georgian",
                            "hiragana",
                            "katakana",
                            "lower-alpha",
                            "lower-greek",
                            "lower-latin",
                            "lower-roman",
                            "none",
                            "upper-alpha",
                            "upper-latin",
                            "upper-roman",
                        ],
                        Literal["circle", "disc", "none", "square"],
                    ]
                ],
            ]
        ] = None,
        items: Optional[Union[Iterable, Var[Iterable]]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[EventType[[], BASE_STATE]] = None,
        on_click: Optional[EventType[[], BASE_STATE]] = None,
        on_context_menu: Optional[EventType[[], BASE_STATE]] = None,
        on_double_click: Optional[EventType[[], BASE_STATE]] = None,
        on_focus: Optional[EventType[[], BASE_STATE]] = None,
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
    ) -> "BaseList":
        """Create a list component.

        Args:
            *children: The children of the component.
            list_style_type: The style of the list. Default to "none".
            items: A list of items to add to the list.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Returns:
            The list component.

        """
        ...

    def add_style(self) -> dict[str, Any] | None: ...

class UnorderedList(BaseList, Ul):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        list_style_type: Optional[
            Union[
                Literal[
                    "armenian",
                    "decimal",
                    "decimal-leading-zero",
                    "georgian",
                    "hiragana",
                    "katakana",
                    "lower-alpha",
                    "lower-greek",
                    "lower-latin",
                    "lower-roman",
                    "none",
                    "upper-alpha",
                    "upper-latin",
                    "upper-roman",
                ],
                Literal["circle", "disc", "none", "square"],
                Var[
                    Union[
                        Literal[
                            "armenian",
                            "decimal",
                            "decimal-leading-zero",
                            "georgian",
                            "hiragana",
                            "katakana",
                            "lower-alpha",
                            "lower-greek",
                            "lower-latin",
                            "lower-roman",
                            "none",
                            "upper-alpha",
                            "upper-latin",
                            "upper-roman",
                        ],
                        Literal["circle", "disc", "none", "square"],
                    ]
                ],
            ]
        ] = None,
        items: Optional[Union[Iterable, Var[Iterable]]] = None,
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
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[EventType[[], BASE_STATE]] = None,
        on_click: Optional[EventType[[], BASE_STATE]] = None,
        on_context_menu: Optional[EventType[[], BASE_STATE]] = None,
        on_double_click: Optional[EventType[[], BASE_STATE]] = None,
        on_focus: Optional[EventType[[], BASE_STATE]] = None,
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
    ) -> "UnorderedList":
        """Create an unordered list component.

        Args:
            *children: The children of the component.
            list_style_type: The style of the list. Default to "none".
            items: A list of items to add to the list.
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
            The list component.

        """
        ...

class OrderedList(BaseList, Ol):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        list_style_type: Optional[
            Union[
                Literal[
                    "armenian",
                    "decimal",
                    "decimal-leading-zero",
                    "georgian",
                    "hiragana",
                    "katakana",
                    "lower-alpha",
                    "lower-greek",
                    "lower-latin",
                    "lower-roman",
                    "none",
                    "upper-alpha",
                    "upper-latin",
                    "upper-roman",
                ],
                Literal["circle", "disc", "none", "square"],
                Var[
                    Union[
                        Literal[
                            "armenian",
                            "decimal",
                            "decimal-leading-zero",
                            "georgian",
                            "hiragana",
                            "katakana",
                            "lower-alpha",
                            "lower-greek",
                            "lower-latin",
                            "lower-roman",
                            "none",
                            "upper-alpha",
                            "upper-latin",
                            "upper-roman",
                        ],
                        Literal["circle", "disc", "none", "square"],
                    ]
                ],
            ]
        ] = None,
        items: Optional[Union[Iterable, Var[Iterable]]] = None,
        reversed: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        start: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        type: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
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
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[EventType[[], BASE_STATE]] = None,
        on_click: Optional[EventType[[], BASE_STATE]] = None,
        on_context_menu: Optional[EventType[[], BASE_STATE]] = None,
        on_double_click: Optional[EventType[[], BASE_STATE]] = None,
        on_focus: Optional[EventType[[], BASE_STATE]] = None,
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
    ) -> "OrderedList":
        """Create an ordered list component.

        Args:
            *children: The children of the component.
            list_style_type: The style of the list. Default to "none".
            items: A list of items to add to the list.
            reversed: Reverses the order of the list.
            start: Specifies the start value of the first list item in an ordered list.
            type: Specifies the kind of marker to use in the list (letters or numbers).
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
            The list component.

        """
        ...

class ListItem(Li):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
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
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[EventType[[], BASE_STATE]] = None,
        on_click: Optional[EventType[[], BASE_STATE]] = None,
        on_context_menu: Optional[EventType[[], BASE_STATE]] = None,
        on_double_click: Optional[EventType[[], BASE_STATE]] = None,
        on_focus: Optional[EventType[[], BASE_STATE]] = None,
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
    ) -> "ListItem":
        """Create a list item component.

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
            **props: The properties of the component.

        Returns:
            The list item component.

        """
        ...

class List(ComponentNamespace):
    item = staticmethod(ListItem.create)
    ordered = staticmethod(OrderedList.create)
    unordered = staticmethod(UnorderedList.create)

    @staticmethod
    def __call__(
        *children,
        list_style_type: Optional[
            Union[
                Literal[
                    "armenian",
                    "decimal",
                    "decimal-leading-zero",
                    "georgian",
                    "hiragana",
                    "katakana",
                    "lower-alpha",
                    "lower-greek",
                    "lower-latin",
                    "lower-roman",
                    "none",
                    "upper-alpha",
                    "upper-latin",
                    "upper-roman",
                ],
                Literal["circle", "disc", "none", "square"],
                Var[
                    Union[
                        Literal[
                            "armenian",
                            "decimal",
                            "decimal-leading-zero",
                            "georgian",
                            "hiragana",
                            "katakana",
                            "lower-alpha",
                            "lower-greek",
                            "lower-latin",
                            "lower-roman",
                            "none",
                            "upper-alpha",
                            "upper-latin",
                            "upper-roman",
                        ],
                        Literal["circle", "disc", "none", "square"],
                    ]
                ],
            ]
        ] = None,
        items: Optional[Union[Iterable, Var[Iterable]]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[EventType[[], BASE_STATE]] = None,
        on_click: Optional[EventType[[], BASE_STATE]] = None,
        on_context_menu: Optional[EventType[[], BASE_STATE]] = None,
        on_double_click: Optional[EventType[[], BASE_STATE]] = None,
        on_focus: Optional[EventType[[], BASE_STATE]] = None,
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
    ) -> "BaseList":
        """Create a list component.

        Args:
            *children: The children of the component.
            list_style_type: The style of the list. Default to "none".
            items: A list of items to add to the list.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Returns:
            The list component.

        """
        ...

list_ns = List()
list_item = list_ns.item
ordered_list = list_ns.ordered
unordered_list = list_ns.unordered

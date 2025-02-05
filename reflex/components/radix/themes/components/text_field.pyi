"""Stub file for reflex/components/radix/themes/components/text_field.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Dict, Literal, Optional, Union, overload

from reflex.components.component import ComponentNamespace
from reflex.components.core.breakpoints import Breakpoints
from reflex.components.el import elements
from reflex.event import EventType, KeyInputInfo
from reflex.style import Style
from reflex.vars.base import Var

from ..base import RadixThemesComponent

LiteralTextFieldSize = Literal["1", "2", "3"]
LiteralTextFieldVariant = Literal["classic", "surface", "soft"]

class TextFieldRoot(elements.Input, RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        size: Optional[
            Union[
                Breakpoints[str, Literal["1", "2", "3"]],
                Literal["1", "2", "3"],
                Var[
                    Union[
                        Breakpoints[str, Literal["1", "2", "3"]], Literal["1", "2", "3"]
                    ]
                ],
            ]
        ] = None,
        variant: Optional[
            Union[
                Literal["classic", "soft", "surface"],
                Var[Literal["classic", "soft", "surface"]],
            ]
        ] = None,
        color_scheme: Optional[
            Union[
                Literal[
                    "amber",
                    "blue",
                    "bronze",
                    "brown",
                    "crimson",
                    "cyan",
                    "gold",
                    "grass",
                    "gray",
                    "green",
                    "indigo",
                    "iris",
                    "jade",
                    "lime",
                    "mint",
                    "orange",
                    "pink",
                    "plum",
                    "purple",
                    "red",
                    "ruby",
                    "sky",
                    "teal",
                    "tomato",
                    "violet",
                    "yellow",
                ],
                Var[
                    Literal[
                        "amber",
                        "blue",
                        "bronze",
                        "brown",
                        "crimson",
                        "cyan",
                        "gold",
                        "grass",
                        "gray",
                        "green",
                        "indigo",
                        "iris",
                        "jade",
                        "lime",
                        "mint",
                        "orange",
                        "pink",
                        "plum",
                        "purple",
                        "red",
                        "ruby",
                        "sky",
                        "teal",
                        "tomato",
                        "violet",
                        "yellow",
                    ]
                ],
            ]
        ] = None,
        radius: Optional[
            Union[
                Literal["full", "large", "medium", "none", "small"],
                Var[Literal["full", "large", "medium", "none", "small"]],
            ]
        ] = None,
        auto_complete: Optional[Union[Var[bool], bool]] = None,
        default_value: Optional[Union[Var[str], str]] = None,
        disabled: Optional[Union[Var[bool], bool]] = None,
        max_length: Optional[Union[Var[int], int]] = None,
        min_length: Optional[Union[Var[int], int]] = None,
        name: Optional[Union[Var[str], str]] = None,
        placeholder: Optional[Union[Var[str], str]] = None,
        read_only: Optional[Union[Var[bool], bool]] = None,
        required: Optional[Union[Var[bool], bool]] = None,
        type: Optional[Union[Var[str], str]] = None,
        value: Optional[Union[Var[Union[float, int, str]], float, int, str]] = None,
        list: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        accept: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        alt: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        auto_focus: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        capture: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        checked: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        default_checked: Optional[Union[Var[bool], bool]] = None,
        dirname: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        form: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        form_action: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        form_enc_type: Optional[
            Union[Var[Union[bool, int, str]], bool, int, str]
        ] = None,
        form_method: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        form_no_validate: Optional[
            Union[Var[Union[bool, int, str]], bool, int, str]
        ] = None,
        form_target: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        max: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        min: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        multiple: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        pattern: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        src: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        step: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        use_map: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
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
        custom_attrs: Optional[Dict[str, Union[Var, Any]]] = None,
        on_blur: Optional[Union[EventType[()], EventType[str]]] = None,
        on_change: Optional[Union[EventType[()], EventType[str]]] = None,
        on_click: Optional[EventType[()]] = None,
        on_context_menu: Optional[EventType[()]] = None,
        on_double_click: Optional[EventType[()]] = None,
        on_focus: Optional[Union[EventType[()], EventType[str]]] = None,
        on_key_down: Optional[
            Union[EventType[()], EventType[str], EventType[str, KeyInputInfo]]
        ] = None,
        on_key_up: Optional[
            Union[EventType[()], EventType[str], EventType[str, KeyInputInfo]]
        ] = None,
        on_mount: Optional[EventType[()]] = None,
        on_mouse_down: Optional[EventType[()]] = None,
        on_mouse_enter: Optional[EventType[()]] = None,
        on_mouse_leave: Optional[EventType[()]] = None,
        on_mouse_move: Optional[EventType[()]] = None,
        on_mouse_out: Optional[EventType[()]] = None,
        on_mouse_over: Optional[EventType[()]] = None,
        on_mouse_up: Optional[EventType[()]] = None,
        on_scroll: Optional[EventType[()]] = None,
        on_unmount: Optional[EventType[()]] = None,
        **props,
    ) -> "TextFieldRoot":
        """Create an Input component.

        Args:
            *children: The children of the component.
            size: Specifies the visible width of a text control
            variant: Variant of text field: "classic" | "surface" | "soft"
            color_scheme: Override theme color for text field
            radius: Override theme radius for text field: "none" | "small" | "medium" | "large" | "full"
            auto_complete: Whether the input should have autocomplete enabled
            default_value: The initial value for a text field
            disabled: Disables the input
            max_length: Specifies the maximum number of characters allowed in the input
            min_length: Specifies the minimum number of characters required in the input
            name: Name of the input, used when sending form data
            placeholder: Placeholder text in the input
            read_only: Indicates whether the input is read-only
            required: Indicates that the input is required
            type: Specifies the type of input
            value: Value of the input
            list: References a datalist for suggested options
            on_change: Fired when the input value changes
            on_focus: Fired when the input gains focus
            on_blur: Fired when the input loses focus
            on_key_down: Fired when a key is pressed down
            on_key_up: Fired when a key is released
            accept: Accepted types of files when the input is file type
            alt: Alternate text for input type="image"
            auto_focus: Automatically focuses the input when the page loads
            capture: Captures media from the user (camera or microphone)
            checked: Indicates whether the input is checked (for checkboxes and radio buttons)
            default_checked: The initial value (for checkboxes and radio buttons)
            dirname: Name part of the input to submit in 'dir' and 'name' pair when form is submitted
            form: Associates the input with a form (by id)
            form_action: URL to send the form data to (for type="submit" buttons)
            form_enc_type: How the form data should be encoded when submitting to the server (for type="submit" buttons)
            form_method: HTTP method to use for sending form data (for type="submit" buttons)
            form_no_validate: Bypasses form validation when submitting (for type="submit" buttons)
            form_target: Specifies where to display the response after submitting the form (for type="submit" buttons)
            max: Specifies the maximum value for the input
            min: Specifies the minimum value for the input
            multiple: Indicates whether multiple values can be entered in an input of the type email or file
            pattern: Regex pattern the input's value must match to be valid
            src: URL for image inputs
            step: Specifies the legal number intervals for an input
            use_map: Name of the image map used with the input
            access_key: Provides a hint for generating a keyboard shortcut for the current element.
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
            The component.
        """
        ...

class TextFieldSlot(RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        color_scheme: Optional[
            Union[
                Literal[
                    "amber",
                    "blue",
                    "bronze",
                    "brown",
                    "crimson",
                    "cyan",
                    "gold",
                    "grass",
                    "gray",
                    "green",
                    "indigo",
                    "iris",
                    "jade",
                    "lime",
                    "mint",
                    "orange",
                    "pink",
                    "plum",
                    "purple",
                    "red",
                    "ruby",
                    "sky",
                    "teal",
                    "tomato",
                    "violet",
                    "yellow",
                ],
                Var[
                    Literal[
                        "amber",
                        "blue",
                        "bronze",
                        "brown",
                        "crimson",
                        "cyan",
                        "gold",
                        "grass",
                        "gray",
                        "green",
                        "indigo",
                        "iris",
                        "jade",
                        "lime",
                        "mint",
                        "orange",
                        "pink",
                        "plum",
                        "purple",
                        "red",
                        "ruby",
                        "sky",
                        "teal",
                        "tomato",
                        "violet",
                        "yellow",
                    ]
                ],
            ]
        ] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, Any]]] = None,
        on_blur: Optional[EventType[()]] = None,
        on_click: Optional[EventType[()]] = None,
        on_context_menu: Optional[EventType[()]] = None,
        on_double_click: Optional[EventType[()]] = None,
        on_focus: Optional[EventType[()]] = None,
        on_mount: Optional[EventType[()]] = None,
        on_mouse_down: Optional[EventType[()]] = None,
        on_mouse_enter: Optional[EventType[()]] = None,
        on_mouse_leave: Optional[EventType[()]] = None,
        on_mouse_move: Optional[EventType[()]] = None,
        on_mouse_out: Optional[EventType[()]] = None,
        on_mouse_over: Optional[EventType[()]] = None,
        on_mouse_up: Optional[EventType[()]] = None,
        on_scroll: Optional[EventType[()]] = None,
        on_unmount: Optional[EventType[()]] = None,
        **props,
    ) -> "TextFieldSlot":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            color_scheme: Override theme color for text field slot
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

class TextField(ComponentNamespace):
    slot = staticmethod(TextFieldSlot.create)

    @staticmethod
    def __call__(
        *children,
        size: Optional[
            Union[
                Breakpoints[str, Literal["1", "2", "3"]],
                Literal["1", "2", "3"],
                Var[
                    Union[
                        Breakpoints[str, Literal["1", "2", "3"]], Literal["1", "2", "3"]
                    ]
                ],
            ]
        ] = None,
        variant: Optional[
            Union[
                Literal["classic", "soft", "surface"],
                Var[Literal["classic", "soft", "surface"]],
            ]
        ] = None,
        color_scheme: Optional[
            Union[
                Literal[
                    "amber",
                    "blue",
                    "bronze",
                    "brown",
                    "crimson",
                    "cyan",
                    "gold",
                    "grass",
                    "gray",
                    "green",
                    "indigo",
                    "iris",
                    "jade",
                    "lime",
                    "mint",
                    "orange",
                    "pink",
                    "plum",
                    "purple",
                    "red",
                    "ruby",
                    "sky",
                    "teal",
                    "tomato",
                    "violet",
                    "yellow",
                ],
                Var[
                    Literal[
                        "amber",
                        "blue",
                        "bronze",
                        "brown",
                        "crimson",
                        "cyan",
                        "gold",
                        "grass",
                        "gray",
                        "green",
                        "indigo",
                        "iris",
                        "jade",
                        "lime",
                        "mint",
                        "orange",
                        "pink",
                        "plum",
                        "purple",
                        "red",
                        "ruby",
                        "sky",
                        "teal",
                        "tomato",
                        "violet",
                        "yellow",
                    ]
                ],
            ]
        ] = None,
        radius: Optional[
            Union[
                Literal["full", "large", "medium", "none", "small"],
                Var[Literal["full", "large", "medium", "none", "small"]],
            ]
        ] = None,
        auto_complete: Optional[Union[Var[bool], bool]] = None,
        default_value: Optional[Union[Var[str], str]] = None,
        disabled: Optional[Union[Var[bool], bool]] = None,
        max_length: Optional[Union[Var[int], int]] = None,
        min_length: Optional[Union[Var[int], int]] = None,
        name: Optional[Union[Var[str], str]] = None,
        placeholder: Optional[Union[Var[str], str]] = None,
        read_only: Optional[Union[Var[bool], bool]] = None,
        required: Optional[Union[Var[bool], bool]] = None,
        type: Optional[Union[Var[str], str]] = None,
        value: Optional[Union[Var[Union[float, int, str]], float, int, str]] = None,
        list: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        accept: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        alt: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        auto_focus: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        capture: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        checked: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        default_checked: Optional[Union[Var[bool], bool]] = None,
        dirname: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        form: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        form_action: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        form_enc_type: Optional[
            Union[Var[Union[bool, int, str]], bool, int, str]
        ] = None,
        form_method: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        form_no_validate: Optional[
            Union[Var[Union[bool, int, str]], bool, int, str]
        ] = None,
        form_target: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        max: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        min: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        multiple: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        pattern: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        src: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        step: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
        use_map: Optional[Union[Var[Union[bool, int, str]], bool, int, str]] = None,
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
        custom_attrs: Optional[Dict[str, Union[Var, Any]]] = None,
        on_blur: Optional[Union[EventType[()], EventType[str]]] = None,
        on_change: Optional[Union[EventType[()], EventType[str]]] = None,
        on_click: Optional[EventType[()]] = None,
        on_context_menu: Optional[EventType[()]] = None,
        on_double_click: Optional[EventType[()]] = None,
        on_focus: Optional[Union[EventType[()], EventType[str]]] = None,
        on_key_down: Optional[
            Union[EventType[()], EventType[str], EventType[str, KeyInputInfo]]
        ] = None,
        on_key_up: Optional[
            Union[EventType[()], EventType[str], EventType[str, KeyInputInfo]]
        ] = None,
        on_mount: Optional[EventType[()]] = None,
        on_mouse_down: Optional[EventType[()]] = None,
        on_mouse_enter: Optional[EventType[()]] = None,
        on_mouse_leave: Optional[EventType[()]] = None,
        on_mouse_move: Optional[EventType[()]] = None,
        on_mouse_out: Optional[EventType[()]] = None,
        on_mouse_over: Optional[EventType[()]] = None,
        on_mouse_up: Optional[EventType[()]] = None,
        on_scroll: Optional[EventType[()]] = None,
        on_unmount: Optional[EventType[()]] = None,
        **props,
    ) -> "TextFieldRoot":
        """Create an Input component.

        Args:
            *children: The children of the component.
            size: Specifies the visible width of a text control
            variant: Variant of text field: "classic" | "surface" | "soft"
            color_scheme: Override theme color for text field
            radius: Override theme radius for text field: "none" | "small" | "medium" | "large" | "full"
            auto_complete: Whether the input should have autocomplete enabled
            default_value: The initial value for a text field
            disabled: Disables the input
            max_length: Specifies the maximum number of characters allowed in the input
            min_length: Specifies the minimum number of characters required in the input
            name: Name of the input, used when sending form data
            placeholder: Placeholder text in the input
            read_only: Indicates whether the input is read-only
            required: Indicates that the input is required
            type: Specifies the type of input
            value: Value of the input
            list: References a datalist for suggested options
            on_change: Fired when the input value changes
            on_focus: Fired when the input gains focus
            on_blur: Fired when the input loses focus
            on_key_down: Fired when a key is pressed down
            on_key_up: Fired when a key is released
            accept: Accepted types of files when the input is file type
            alt: Alternate text for input type="image"
            auto_focus: Automatically focuses the input when the page loads
            capture: Captures media from the user (camera or microphone)
            checked: Indicates whether the input is checked (for checkboxes and radio buttons)
            default_checked: The initial value (for checkboxes and radio buttons)
            dirname: Name part of the input to submit in 'dir' and 'name' pair when form is submitted
            form: Associates the input with a form (by id)
            form_action: URL to send the form data to (for type="submit" buttons)
            form_enc_type: How the form data should be encoded when submitting to the server (for type="submit" buttons)
            form_method: HTTP method to use for sending form data (for type="submit" buttons)
            form_no_validate: Bypasses form validation when submitting (for type="submit" buttons)
            form_target: Specifies where to display the response after submitting the form (for type="submit" buttons)
            max: Specifies the maximum value for the input
            min: Specifies the minimum value for the input
            multiple: Indicates whether multiple values can be entered in an input of the type email or file
            pattern: Regex pattern the input's value must match to be valid
            src: URL for image inputs
            step: Specifies the legal number intervals for an input
            use_map: Name of the image map used with the input
            access_key: Provides a hint for generating a keyboard shortcut for the current element.
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
            The component.
        """
        ...

input = text_field = TextField()

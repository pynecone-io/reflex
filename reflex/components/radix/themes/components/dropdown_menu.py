"""Interactive components provided by @radix-ui/themes."""

from typing import Dict, List, Literal, Union

from reflex.components.component import ComponentNamespace
from reflex.components.core.breakpoints import Responsive
from reflex.event import EventHandler
from reflex.ivars.base import ImmutableVar

from ..base import (
    LiteralAccentColor,
    RadixThemesComponent,
    RadixThemesTriggerComponent,
)

LiteralDirType = Literal["ltr", "rtl"]

LiteralSizeType = Literal["1", "2"]

LiteralVariantType = Literal["solid", "soft"]

LiteralSideType = Literal["top", "right", "bottom", "left"]

LiteralAlignType = Literal["start", "center", "end"]


LiteralStickyType = Literal[
    "partial",
    "always",
]


class DropdownMenuRoot(RadixThemesComponent):
    """The Dropdown Menu Root Component."""

    tag = "DropdownMenu.Root"

    # The open state of the dropdown menu when it is initially rendered. Use when you do not need to control its open state.
    default_open: ImmutableVar[bool]

    # The controlled open state of the dropdown menu. Must be used in conjunction with onOpenChange.
    open: ImmutableVar[bool]

    # The modality of the dropdown menu. When set to true, interaction with outside elements will be disabled and only menu content will be visible to screen readers. Defaults to True.
    modal: ImmutableVar[bool]

    # The reading direction of submenus when applicable. If omitted, inherits globally from DirectionProvider or assumes LTR (left-to-right) reading mode.
    dir: ImmutableVar[LiteralDirType]

    _invalid_children: List[str] = ["DropdownMenuItem"]

    # Fired when the open state changes.
    on_open_change: EventHandler[lambda e0: [e0]]


class DropdownMenuTrigger(RadixThemesTriggerComponent):
    """The button that toggles the dropdown menu."""

    tag = "DropdownMenu.Trigger"

    # Change the default rendered element for the one passed as a child, merging their props and behavior. Defaults to False.
    as_child: ImmutableVar[bool]

    _valid_parents: List[str] = ["DropdownMenuRoot"]

    _invalid_children: List[str] = ["DropdownMenuContent"]


class DropdownMenuContent(RadixThemesComponent):
    """The Dropdown Menu Content component that pops out when the dropdown menu is open."""

    tag = "DropdownMenu.Content"

    # Dropdown Menu Content size "1" - "2"
    size: ImmutableVar[Responsive[LiteralSizeType]]

    # Variant of Dropdown Menu Content: "solid" | "soft"
    variant: ImmutableVar[LiteralVariantType]

    # Override theme color for Dropdown Menu Content
    color_scheme: ImmutableVar[LiteralAccentColor]

    # Renders the Dropdown Menu Content in higher contrast
    high_contrast: ImmutableVar[bool]

    # Change the default rendered element for the one passed as a child, merging their props and behavior. Defaults to False.
    as_child: ImmutableVar[bool]

    # When True, keyboard navigation will loop from last item to first, and vice versa. Defaults to False.
    loop: ImmutableVar[bool]

    # Used to force mounting when more control is needed. Useful when controlling animation with React animation libraries.
    force_mount: ImmutableVar[bool]

    # The preferred side of the trigger to render against when open. Will be reversed when collisions occur and `avoid_collisions` is enabled.The position of the tooltip. Defaults to "top".
    side: ImmutableVar[LiteralSideType]

    # The distance in pixels from the trigger. Defaults to 0.
    side_offset: ImmutableVar[Union[float, int]]

    # The preferred alignment against the trigger. May change when collisions occur. Defaults to "center".
    align: ImmutableVar[LiteralAlignType]

    # An offset in pixels from the "start" or "end" alignment options.
    align_offset: ImmutableVar[Union[float, int]]

    # When true, overrides the side and align preferences to prevent collisions with boundary edges. Defaults to True.
    avoid_collisions: ImmutableVar[bool]

    # The distance in pixels from the boundary edges where collision detection should occur. Accepts a number (same for all sides), or a partial padding object, for example: { "top": 20, "left": 20 }. Defaults to 0.
    collision_padding: ImmutableVar[Union[float, int, Dict[str, Union[float, int]]]]

    # The padding between the arrow and the edges of the content. If your content has border-radius, this will prevent it from overflowing the corners. Defaults to 0.
    arrow_padding: ImmutableVar[Union[float, int]]

    # The sticky behavior on the align axis. "partial" will keep the content in the boundary as long as the trigger is at least partially in the boundary whilst "always" will keep the content in the boundary regardless. Defaults to "partial".
    sticky: ImmutableVar[LiteralStickyType]

    # Whether to hide the content when the trigger becomes fully occluded. Defaults to False.
    hide_when_detached: ImmutableVar[bool]

    # Fired when the dialog is closed.
    on_close_auto_focus: EventHandler[lambda e0: [e0]]

    # Fired when the escape key is pressed.
    on_escape_key_down: EventHandler[lambda e0: [e0]]

    # Fired when the pointer is down outside the dialog.
    on_pointer_down_outside: EventHandler[lambda e0: [e0]]

    # Fired when focus moves outside the dialog.
    on_focus_outside: EventHandler[lambda e0: [e0]]

    # Fired when the pointer interacts outside the dialog.
    on_interact_outside: EventHandler[lambda e0: [e0]]


class DropdownMenuSubTrigger(RadixThemesTriggerComponent):
    """An item that opens a submenu."""

    tag = "DropdownMenu.SubTrigger"

    # Change the default rendered element for the one passed as a child, merging their props and behavior. Defaults to False.
    as_child: ImmutableVar[bool]

    # When true, prevents the user from interacting with the item.
    disabled: ImmutableVar[bool]

    # Optional text used for typeahead purposes. By default the typeahead behavior will use the .textContent of the item. Use this when the content is complex, or you have non-textual content inside.
    text_value: ImmutableVar[str]

    _valid_parents: List[str] = ["DropdownMenuContent", "DropdownMenuSub"]


class DropdownMenuSub(RadixThemesComponent):
    """Contains all the parts of a submenu."""

    tag = "DropdownMenu.Sub"

    # The controlled open state of the submenu. Must be used in conjunction with `on_open_change`.
    open: ImmutableVar[bool]

    # The open state of the submenu when it is initially rendered. Use when you do not need to control its open state.
    default_open: ImmutableVar[bool]

    # Fired when the open state changes.
    on_open_change: EventHandler[lambda e0: [e0.target.value]]


class DropdownMenuSubContent(RadixThemesComponent):
    """The component that pops out when a submenu is open. Must be rendered inside DropdownMenuSub."""

    tag = "DropdownMenu.SubContent"

    # Change the default rendered element for the one passed as a child, merging their props and behavior. Defaults to False.
    as_child: ImmutableVar[bool]

    # When True, keyboard navigation will loop from last item to first, and vice versa. Defaults to False.
    loop: ImmutableVar[bool]

    # Used to force mounting when more control is needed. Useful when controlling animation with React animation libraries.
    force_mount: ImmutableVar[bool]

    # The distance in pixels from the trigger. Defaults to 0.
    side_offset: ImmutableVar[Union[float, int]]

    # An offset in pixels from the "start" or "end" alignment options.
    align_offset: ImmutableVar[Union[float, int]]

    # When true, overrides the side and align preferences to prevent collisions with boundary edges. Defaults to True.
    avoid_collisions: ImmutableVar[bool]

    # The distance in pixels from the boundary edges where collision detection should occur. Accepts a number (same for all sides), or a partial padding object, for example: { "top": 20, "left": 20 }. Defaults to 0.
    collision_padding: ImmutableVar[Union[float, int, Dict[str, Union[float, int]]]]

    # The padding between the arrow and the edges of the content. If your content has border-radius, this will prevent it from overflowing the corners. Defaults to 0.
    arrow_padding: ImmutableVar[Union[float, int]]

    # The sticky behavior on the align axis. "partial" will keep the content in the boundary as long as the trigger is at least partially in the boundary whilst "always" will keep the content in the boundary regardless. Defaults to "partial".
    sticky: ImmutableVar[LiteralStickyType]

    # Whether to hide the content when the trigger becomes fully occluded. Defaults to False.
    hide_when_detached: ImmutableVar[bool]

    _valid_parents: List[str] = ["DropdownMenuSub"]

    # Fired when the escape key is pressed.
    on_escape_key_down: EventHandler[lambda e0: [e0]]

    # Fired when the pointer is down outside the dialog.
    on_pointer_down_outside: EventHandler[lambda e0: [e0]]

    # Fired when focus moves outside the dialog.
    on_focus_outside: EventHandler[lambda e0: [e0]]

    # Fired when the pointer interacts outside the dialog.
    on_interact_outside: EventHandler[lambda e0: [e0]]


class DropdownMenuItem(RadixThemesComponent):
    """The Dropdown Menu Item Component."""

    tag = "DropdownMenu.Item"

    # Override theme color for Dropdown Menu Item
    color_scheme: ImmutableVar[LiteralAccentColor]

    # Shortcut to render a menu item as a link
    shortcut: ImmutableVar[str]

    # Change the default rendered element for the one passed as a child, merging their props and behavior. Defaults to False.
    as_child: ImmutableVar[bool]

    # When true, prevents the user from interacting with the item.
    disabled: ImmutableVar[bool]

    # Optional text used for typeahead purposes. By default the typeahead behavior will use the .textContent of the item. Use this when the content is complex, or you have non-textual content inside.
    text_value: ImmutableVar[str]

    _valid_parents: List[str] = ["DropdownMenuContent", "DropdownMenuSubContent"]

    # Fired when the item is selected.
    on_select: EventHandler[lambda e0: [e0.target.value]]


class DropdownMenuSeparator(RadixThemesComponent):
    """Dropdown Menu Separator Component. Used to visually separate items in the dropdown menu."""

    tag = "DropdownMenu.Separator"


class DropdownMenu(ComponentNamespace):
    """DropdownMenu components namespace."""

    root = staticmethod(DropdownMenuRoot.create)
    trigger = staticmethod(DropdownMenuTrigger.create)
    content = staticmethod(DropdownMenuContent.create)
    sub_trigger = staticmethod(DropdownMenuSubTrigger.create)
    sub = staticmethod(DropdownMenuSub.create)
    sub_content = staticmethod(DropdownMenuSubContent.create)
    item = staticmethod(DropdownMenuItem.create)
    separator = staticmethod(DropdownMenuSeparator.create)


menu = dropdown_menu = DropdownMenu()

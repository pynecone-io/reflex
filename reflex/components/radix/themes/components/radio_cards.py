"""Radio component from Radix Themes."""

from types import SimpleNamespace
from typing import Literal, Union

from reflex.components.core.breakpoints import Responsive
from reflex.event import EventHandler
from reflex.ivars.base import ImmutableVar

from ..base import LiteralAccentColor, RadixThemesComponent


class RadioCardsRoot(RadixThemesComponent):
    """Root element for RadioCards component."""

    tag = "RadioCards.Root"

    # Change the default rendered element for the one passed as a child, merging their props and behavior.
    as_child: ImmutableVar[bool]

    # The size of the checkbox cards: "1" | "2" | "3"
    size: ImmutableVar[Responsive[Literal["1", "2", "3"]]]

    # Variant of button: "classic" | "surface" | "soft"
    variant: ImmutableVar[Literal["classic", "surface"]]

    # Override theme color for button
    color_scheme: ImmutableVar[LiteralAccentColor]

    # Uses a higher contrast color for the component.
    high_contrast: ImmutableVar[bool]

    # The number of columns:
    columns: ImmutableVar[
        Responsive[Union[str, Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]]]
    ]

    # The gap between the checkbox cards:
    gap: ImmutableVar[
        Responsive[Union[str, Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]]]
    ]

    default_value: ImmutableVar[str]

    # The controlled value of the radio item to check. Should be used in conjunction with onValueChange.
    value: ImmutableVar[str]

    # The name of the group. Submitted with its owning form as part of a name/value pair.
    name: ImmutableVar[str]

    # When true, prevents the user from interacting with radio items.
    disabled: ImmutableVar[bool]

    # When true, indicates that the user must check a radio item before the owning form can be submitted.
    required: ImmutableVar[bool]

    # The orientation of the component.
    orientation: ImmutableVar[Literal["horizontal", "vertical", "undefined"]]

    # The reading direction of the radio group. If omitted,
    # inherits globally from DirectionProvider or assumes LTR (left-to-right) reading mode.
    dir: ImmutableVar[Literal["ltr", "rtl"]]

    # When true, keyboard navigation will loop from last item to first, and vice versa.
    loop: ImmutableVar[bool]

    # Event handler called when the value changes.
    on_value_change: EventHandler[lambda e0: [e0]]


class RadioCardsItem(RadixThemesComponent):
    """Item element for RadioCards component."""

    tag = "RadioCards.Item"

    # Change the default rendered element for the one passed as a child, merging their props and behavior.
    as_child: ImmutableVar[bool]

    # The value given as data when submitted with a name.
    value: ImmutableVar[str]

    # When true, prevents the user from interacting with the radio item.
    disabled: ImmutableVar[bool]

    # When true, indicates that the user must check the radio item before the owning form can be submitted.
    required: ImmutableVar[bool]


class RadioCards(SimpleNamespace):
    """RadioCards components namespace."""

    root = staticmethod(RadioCardsRoot.create)
    item = staticmethod(RadioCardsItem.create)


radio_cards = RadioCards()

"""Components for the Radix CheckboxCards component."""

from types import SimpleNamespace
from typing import Literal, Union

from reflex.components.core.breakpoints import Responsive
from reflex.ivars.base import ImmutableVar

from ..base import LiteralAccentColor, RadixThemesComponent


class CheckboxCardsRoot(RadixThemesComponent):
    """Root element for a CheckboxCards component."""

    tag = "CheckboxCards.Root"

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


class CheckboxCardsItem(RadixThemesComponent):
    """An item in the CheckboxCards component."""

    tag = "CheckboxCards.Item"


class CheckboxCards(SimpleNamespace):
    """CheckboxCards components namespace."""

    root = staticmethod(CheckboxCardsRoot.create)
    item = staticmethod(CheckboxCardsItem.create)


checkbox_cards = CheckboxCards()

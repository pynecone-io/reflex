"""Interactive components provided by @radix-ui/themes."""

from typing import Literal

from reflex.components.core.breakpoints import Responsive
from reflex.components.el import elements
from reflex.ivars.base import ImmutableVar

from ..base import (
    LiteralAccentColor,
    LiteralRadius,
    LiteralVariant,
    RadixLoadingProp,
    RadixThemesComponent,
)

LiteralButtonSize = Literal["1", "2", "3", "4"]


class Button(elements.Button, RadixLoadingProp, RadixThemesComponent):
    """Trigger an action or event, such as submitting a form or displaying a dialog."""

    tag = "Button"

    # Change the default rendered element for the one passed as a child, merging their props and behavior.
    as_child: ImmutableVar[bool]

    # Button size "1" - "4"
    size: ImmutableVar[Responsive[LiteralButtonSize]]

    # Variant of button: "solid" | "soft" | "outline" | "ghost"
    variant: ImmutableVar[LiteralVariant]

    # Override theme color for button
    color_scheme: ImmutableVar[LiteralAccentColor]

    # Whether to render the button with higher contrast color against background
    high_contrast: ImmutableVar[bool]

    # Override theme radius for button: "none" | "small" | "medium" | "large" | "full"
    radius: ImmutableVar[LiteralRadius]


button = Button.create

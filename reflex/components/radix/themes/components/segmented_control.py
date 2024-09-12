"""SegmentedControl from Radix Themes."""

from __future__ import annotations

from types import SimpleNamespace
from typing import List, Literal, Union

from reflex.components.core.breakpoints import Responsive
from reflex.event import EventHandler
from reflex.ivars.base import ImmutableVar

from ..base import LiteralAccentColor, RadixThemesComponent


class SegmentedControlRoot(RadixThemesComponent):
    """Root element for a SegmentedControl component."""

    tag = "SegmentedControl.Root"

    # The size of the segmented control: "1" | "2" | "3"
    size: ImmutableVar[Responsive[Literal["1", "2", "3"]]]

    # Variant of button: "classic" | "surface"
    variant: ImmutableVar[Literal["classic", "surface"]]

    type: ImmutableVar[Literal["single", "multiple"]]

    # Override theme color for button
    color_scheme: ImmutableVar[LiteralAccentColor]

    # The radius of the segmented control: "none" | "small" | "medium" | "large" | "full"
    radius: ImmutableVar[Literal["none", "small", "medium", "large", "full"]]

    # The default value of the segmented control.
    default_value: ImmutableVar[Union[str, List[str]]]

    value: ImmutableVar[Union[str, List[str]]]

    on_change: EventHandler[lambda e0: [e0]]

    _rename_props = {"onChange": "onValueChange"}


class SegmentedControlItem(RadixThemesComponent):
    """An item in the SegmentedControl component."""

    tag = "SegmentedControl.Item"

    # The value of the item.
    value: ImmutableVar[str]

    _valid_parents: List[str] = ["SegmentedControlRoot"]


class SegmentedControl(SimpleNamespace):
    """SegmentedControl components namespace."""

    root = staticmethod(SegmentedControlRoot.create)
    item = staticmethod(SegmentedControlItem.create)


segmented_control = SegmentedControl()

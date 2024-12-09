"""Stub file for reflex/components/recharts/recharts.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Dict, Literal, Optional, Union, overload

from reflex.components.component import Component, MemoizationLeaf, NoSSRComponent
from reflex.event import BASE_STATE, EventType
from reflex.style import Style
from reflex.vars.base import Var

class Recharts(Component):
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
        custom_attrs: Optional[Dict[str, Union[Var, Any]]] = None,
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
    ) -> "Recharts":
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

class RechartsCharts(NoSSRComponent, MemoizationLeaf):
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
        custom_attrs: Optional[Dict[str, Union[Var, Any]]] = None,
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
    ) -> "RechartsCharts":
        """Create a new memoization leaf component.

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
            The memoization leaf
        """
        ...

LiteralAnimationEasing = Literal["ease", "ease-in", "ease-out", "ease-in-out", "linear"]
LiteralIfOverflow = Literal["discard", "hidden", "visible", "extendDomain"]
LiteralShape = Literal[
    "square", "circle", "cross", "diamond", "star", "triangle", "wye"
]
LiteralLineType = Literal["joint", "fitting"]
LiteralOrientation = Literal["top", "bottom", "left", "right", "middle"]
LiteralOrientationLeftRightMiddle = Literal["left", "right", "middle"]
LiteralOrientationTopBottom = Literal["top", "bottom"]
LiteralOrientationLeftRight = Literal["left", "right"]
LiteralOrientationTopBottomLeftRight = Literal["top", "bottom", "left", "right"]
LiteralScale = Literal[
    "auto",
    "linear",
    "pow",
    "sqrt",
    "log",
    "identity",
    "time",
    "band",
    "point",
    "ordinal",
    "quantile",
    "quantize",
    "utc",
    "sequential",
    "threshold",
]
LiteralTextAnchor = Literal["start", "middle", "end"]
LiteralLayout = Literal["horizontal", "vertical"]
LiteralPolarRadiusType = Literal["number", "category"]
LiteralGridType = Literal["polygon", "circle"]
LiteralPosition = Literal[
    "top",
    "left",
    "right",
    "bottom",
    "inside",
    "outside",
    "insideLeft",
    "insideRight",
    "insideTop",
    "insideBottom",
    "insideTopLeft",
    "insideBottomLeft",
    "insideTopRight",
    "insideBottomRight",
    "insideStart",
    "insideEnd",
    "end",
    "center",
]
LiteralIconType = Literal[
    "line",
    "plainline",
    "square",
    "rect",
    "circle",
    "cross",
    "diamond",
    "star",
    "triangle",
    "wye",
]
LiteralLegendType = Literal[
    "line",
    "plainline",
    "square",
    "rect",
    "circle",
    "cross",
    "diamond",
    "star",
    "triangle",
    "wye",
    "none",
]
LiteralLegendAlign = Literal["left", "center", "right"]
LiteralVerticalAlign = Literal["top", "middle", "bottom"]
LiteralStackOffset = Literal["expand", "none", "wiggle", "silhouette"]
LiteralBarChartStackOffset = Literal["expand", "none", "wiggle", "silhouette", "sign"]
LiteralComposedChartBaseValue = Literal["dataMin", "dataMax", "auto"]
LiteralAxisType = Literal["number", "category"]
LiteralAreaType = Literal[
    "basis",
    "basisClosed",
    "basisOpen",
    "bumpX",
    "bumpY",
    "bump",
    "linear",
    "linearClosed",
    "natural",
    "monotoneX",
    "monotoneY",
    "monotone",
    "step",
    "stepBefore",
    "stepAfter",
]
LiteralDirection = Literal["x", "y"]
LiteralInterval = Literal["preserveStart", "preserveEnd", "preserveStartEnd"]
LiteralIntervalAxis = Literal[
    "preserveStart", "preserveEnd", "preserveStartEnd", "equidistantPreserveStart"
]
LiteralSyncMethod = Literal["index", "value"]

"""Polar charts in Recharts."""

from __future__ import annotations

from typing import Any, Dict, List, Union

from reflex.constants import EventTriggers
from reflex.constants.colors import Color
from reflex.event import EventHandler, empty_event
from reflex.vars.base import LiteralVar, Var

from .recharts import (
    LiteralAnimationEasing,
    LiteralGridType,
    LiteralLegendType,
    LiteralPolarRadiusType,
    LiteralScale,
    Recharts,
)


class Pie(Recharts):
    """A Pie chart component in Recharts."""

    tag = "Pie"

    alias = "RechartsPie"

    # data
    data: Var[List[Dict[str, Any]]]

    # The key of each sector's value.
    data_key: Var[Union[str, int]]

    # The x-coordinate of center. If set a percentage, the final value is obtained by multiplying the percentage of container width.
    cx: Var[Union[int, str]]

    # The y-coordinate of center. If set a percentage, the final value is obtained by multiplying the percentage of container height.
    cy: Var[Union[int, str]]

    # The inner radius of pie, which can be set to a percent value.
    inner_radius: Var[Union[int, str]]

    # The outer radius of pie, which can be set to a percent value.
    outer_radius: Var[Union[int, str]]

    # The angle of first sector.
    start_angle: Var[int]

    # The direction of sectors. 1 means clockwise and -1 means anticlockwise.
    end_angle: Var[int]

    # The minimum angle of each unzero data.
    min_angle: Var[int]

    # The angle between two sectors.
    padding_angle: Var[int]

    # The key of each sector's name.
    name_key: Var[str]

    # The type of icon in legend. If set to 'none', no legend item will be rendered.
    legend_type: Var[LiteralLegendType]

    # If false set, labels will not be drawn.
    label: Var[bool] = False  # type: ignore

    # If false set, label lines will not be drawn.
    label_line: Var[bool]

    # Valid children components
    _valid_children: List[str] = ["Cell", "LabelList"]

    # Stoke color
    stroke: Var[Union[str, Color]] = LiteralVar.create(Color("accent", 9))

    # Fill color
    fill: Var[Union[str, Color]] = LiteralVar.create(Color("accent", 3))

    def get_event_triggers(self) -> dict[str, Union[Var, Any]]:
        """Get the event triggers that pass the component's value to the handler.

        Returns:
            A dict mapping the event trigger to the var that is passed to the handler.
        """
        return {
            EventTriggers.ON_CLICK: lambda: [],
            EventTriggers.ON_MOUSE_MOVE: lambda: [],
            EventTriggers.ON_MOUSE_OVER: lambda: [],
            EventTriggers.ON_MOUSE_OUT: lambda: [],
            EventTriggers.ON_MOUSE_ENTER: lambda: [],
            EventTriggers.ON_MOUSE_LEAVE: lambda: [],
        }


class Radar(Recharts):
    """A Radar chart component in Recharts."""

    tag = "Radar"

    alias = "RechartsRadar"

    # The key of a group of data which should be unique in a radar chart.
    data_key: Var[Union[str, int]]

    # The coordinates of all the vertexes of the radar shape, like [{ x, y }].
    points: Var[List[Dict[str, Any]]]

    # If false set, dots will not be drawn. Default: True
    dot: Var[bool]

    # Stoke color. Default: rx.color("accent", 9)
    stroke: Var[Union[str, Color]] = LiteralVar.create(Color("accent", 9))

    # Fill color. Default: rx.color("accent", 3)
    fill: Var[str] = LiteralVar.create(Color("accent", 3))

    # opacity. Default: 0.6
    fill_opacity: Var[float] = LiteralVar.create(0.6)

    # The type of icon in legend. If set to 'none', no legend item will be rendered. Default: "rect"
    legend_type: Var[LiteralLegendType]

    # If false set, labels will not be drawn. Default: True
    label: Var[bool]

    # If set false, animation of polygon will be disabled. Default: True in CSR, and False in SSR
    is_animation_active: Var[bool]

    # Specifies when the animation should begin, the unit of this option is ms. Default: 0
    animation_begin: Var[int]

    # Specifies the duration of animation, the unit of this option is ms. Default: 1500
    animation_duration: Var[int]

    # The type of easing function. 'ease' | 'ease-in' | 'ease-out' | 'ease-in-out' | 'linear'. Default: "ease"
    animation_easing: Var[LiteralAnimationEasing]

    # Valid children components
    _valid_children: List[str] = ["LabelList"]

    def get_event_triggers(self) -> dict[str, Union[Var, Any]]:
        """Get the event triggers that pass the component's value to the handler.

        Returns:
            A dict mapping the event trigger to the var that is passed to the handler.
        """
        return {
            EventTriggers.ON_ANIMATION_START: lambda: [],
            EventTriggers.ON_ANIMATION_END: lambda: [],
        }


class RadialBar(Recharts):
    """A RadialBar chart component in Recharts."""

    tag = "RadialBar"

    alias = "RechartsRadialBar"

    # The key of a group of data which should be unique to show the meaning of angle axis.
    data_key: Var[Union[str, int]]

    # Min angle of each bar. A positive value between 0 and 360.
    min_angle: Var[int]

    # Type of legend
    legend_type: Var[str]

    # If false set, labels will not be drawn.
    label: Var[Union[bool, Dict[str, Any]]]

    # If false set, background sector will not be drawn.
    background: Var[Union[bool, Dict[str, Any]]]

    # If set false, animation of radial bars will be disabled. By default true in CSR, and false in SSR
    is_animation_active: Var[bool]

    # Specifies when the animation should begin, the unit of this option is ms. By default 0
    animation_begin: Var[int]

    # Specifies the duration of animation, the unit of this option is ms. By default 1500
    animation_duration: Var[int]

    # The type of easing function. 'ease' | 'ease-in' | 'ease-out' | 'ease-in-out' | 'linear'. By default 'ease'
    animation_easing: Var[LiteralAnimationEasing]

    # Valid children components
    _valid_children: List[str] = ["Cell", "LabelList"]

    def get_event_triggers(self) -> dict[str, Union[Var, Any]]:
        """Get the event triggers that pass the component's value to the handler.

        Returns:
            A dict mapping the event trigger to the var that is passed to the handler.
        """
        return {
            EventTriggers.ON_CLICK: lambda: [],
            EventTriggers.ON_MOUSE_MOVE: lambda: [],
            EventTriggers.ON_MOUSE_OVER: lambda: [],
            EventTriggers.ON_MOUSE_OUT: lambda: [],
            EventTriggers.ON_MOUSE_ENTER: lambda: [],
            EventTriggers.ON_MOUSE_LEAVE: lambda: [],
            EventTriggers.ON_ANIMATION_START: lambda: [],
            EventTriggers.ON_ANIMATION_END: lambda: [],
        }


class PolarAngleAxis(Recharts):
    """A PolarAngleAxis component in Recharts."""

    tag = "PolarAngleAxis"

    alias = "RechartsPolarAngleAxis"

    # The key of a group of data which should be unique to show the meaning of angle axis.
    data_key: Var[Union[str, int]]

    # The x-coordinate of center. If set a percentage, the final value is obtained by multiplying the percentage of container width.
    cx: Var[Union[int, str]]

    # The y-coordinate of center. If set a percentage, the final value is obtained by multiplying the percentage of container height.
    cy: Var[Union[int, str]]

    # The outer radius of circle grid. If set a percentage, the final value is obtained by multiplying the percentage of maxRadius which is calculated by the width, height, cx, cy.
    radius: Var[Union[int, str]]

    # If false set, axis line will not be drawn. If true set, axis line will be drawn which have the props calculated internally. If object set, axis line will be drawn which have the props mergered by the internal calculated props and the option. Default: True
    axis_line: Var[Union[bool, Dict[str, Any]]]

    # The type of axis line. Default: "polygon"
    axis_line_type: Var[LiteralGridType]

    # If false set, tick lines will not be drawn. If true set, tick lines will be drawn which have the props calculated internally. If object set, tick lines will be drawn which have the props mergered by the internal calculated props and the option. Default: False
    tick_line: Var[Union[bool, Dict[str, Any]]] = LiteralVar.create(False)

    # If false set, ticks will not be drawn. If true set, ticks will be drawn which have the props calculated internally. If object set, ticks will be drawn which have the props mergered by the internal calculated props and the option. Default: True
    tick: Var[Union[bool, Dict[str, Any]]]

    # The array of every tick's value and angle.
    ticks: Var[List[Dict[str, Any]]]

    # The orientation of axis text. Default: "outer"
    orientation: Var[str]

    # The stroke color of axis. Default: rx.color("gray", 10)
    stroke: Var[Union[str, Color]] = LiteralVar.create(Color("gray", 10))

    # Allow the axis has duplicated categorys or not when the type of axis is "category". Default: True
    allow_duplicated_category: Var[bool]

    # Valid children components.
    _valid_children: List[str] = ["Label"]

    # The customized event handler of click on the ticks of this axis.
    on_click: EventHandler[empty_event]

    # The customized event handler of mousedown on the the ticks of this axis.
    on_mouse_down: EventHandler[empty_event]

    # The customized event handler of mouseup on the ticks of this axis.
    on_mouse_up: EventHandler[empty_event]

    # The customized event handler of mousemove on the ticks of this axis.
    on_mouse_move: EventHandler[empty_event]

    # The customized event handler of mouseover on the ticks of this axis.
    on_mouse_over: EventHandler[empty_event]

    # The customized event handler of mouseout on the ticks of this axis.
    on_mouse_out: EventHandler[empty_event]

    # The customized event handler of moustenter on the ticks of this axis.
    on_mouse_enter: EventHandler[empty_event]

    # The customized event handler of mouseleave on the ticks of this axis.
    on_mouse_leave: EventHandler[empty_event]


class PolarGrid(Recharts):
    """A PolarGrid component in Recharts."""

    tag = "PolarGrid"

    alias = "RechartsPolarGrid"

    # The x-coordinate of center.
    cx: Var[int]

    # The y-coordinate of center.
    cy: Var[int]

    # The radius of the inner polar grid.
    inner_radius: Var[int]

    # The radius of the outer polar grid.
    outer_radius: Var[int]

    # The array of every line grid's angle.
    polar_angles: Var[List[int]]

    # The array of every line grid's radius.
    polar_radius: Var[List[int]]

    # The type of polar grids. 'polygon' | 'circle'. Default: "polygon"
    grid_type: Var[LiteralGridType]

    # The stroke color of grid. Default: rx.color("gray", 10)
    stroke: Var[Union[str, Color]] = LiteralVar.create(Color("gray", 10))

    # Valid children components
    _valid_children: List[str] = ["RadarChart", "RadiarBarChart"]


class PolarRadiusAxis(Recharts):
    """A PolarRadiusAxis component in Recharts."""

    tag = "PolarRadiusAxis"

    alias = "RechartsPolarRadiusAxis"

    # The angle of radial direction line to display axis text.
    angle: Var[int]

    # The type of axis line. 'number' | 'category'
    type_: Var[LiteralPolarRadiusType]

    # Allow the axis has duplicated categorys or not when the type of axis is "category".
    allow_duplicated_category: Var[bool]

    # The x-coordinate of center.
    cx: Var[Union[int, str]]

    # The y-coordinate of center.
    cy: Var[Union[int, str]]

    # If set to true, the ticks of this axis are reversed.
    reversed: Var[bool]

    # The orientation of axis text.
    orientation: Var[str]

    # If false set, axis line will not be drawn. If true set, axis line will be drawn which have the props calculated internally. If object set, axis line will be drawn which have the props mergered by the internal calculated props and the option.
    axis_line: Var[Union[bool, Dict[str, Any]]]

    # The width or height of tick.
    tick: Var[Union[int, str]]

    # The count of ticks.
    tick_count: Var[int]

    # If 'auto' set, the scale funtion is linear scale. 'auto' | 'linear' | 'pow' | 'sqrt' | 'log' | 'identity' | 'time' | 'band' | 'point' | 'ordinal' | 'quantile' | 'quantize' | 'utc' | 'sequential' | 'threshold'
    scale: Var[LiteralScale]

    # Valid children components
    _valid_children: List[str] = ["Label"]

    # The domain of the polar radius axis, specifying the minimum and maximum values.
    domain: Var[List[int]] = LiteralVar.create([0, 250])

    # The stroke color of axis
    stroke: Var[Union[str, Color]] = LiteralVar.create(Color("gray", 10))

    def get_event_triggers(self) -> dict[str, Union[Var, Any]]:
        """Get the event triggers that pass the component's value to the handler.

        Returns:
            A dict mapping the event trigger to the var that is passed to the handler.
        """
        return {
            EventTriggers.ON_CLICK: lambda: [],
            EventTriggers.ON_MOUSE_MOVE: lambda: [],
            EventTriggers.ON_MOUSE_OVER: lambda: [],
            EventTriggers.ON_MOUSE_OUT: lambda: [],
            EventTriggers.ON_MOUSE_ENTER: lambda: [],
            EventTriggers.ON_MOUSE_LEAVE: lambda: [],
        }


pie = Pie.create
radar = Radar.create
radial_bar = RadialBar.create
polar_angle_axis = PolarAngleAxis.create
polar_grid = PolarGrid.create
polar_radius_axis = PolarRadiusAxis.create

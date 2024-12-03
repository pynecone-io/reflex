"""Stub file for reflex/components/datadisplay/dataeditor.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from enum import Enum
from typing import Any, Dict, List, Literal, Optional, Union, overload

from typing_extensions import TypedDict

from reflex.base import Base
from reflex.components.component import NoSSRComponent
from reflex.event import BASE_STATE, EventType
from reflex.style import Style
from reflex.utils.imports import ImportDict
from reflex.utils.serializers import serializer
from reflex.vars.base import Var

class GridColumnIcons(Enum):
    Array = "array"
    AudioUri = "audio_uri"
    Boolean = "boolean"
    HeaderCode = "code"
    Date = "date"
    Email = "email"
    Emoji = "emoji"
    GeoDistance = "geo_distance"
    IfThenElse = "if_then_else"
    Image = "image"
    JoinStrings = "join_strings"
    Lookup = "lookup"
    Markdown = "markdown"
    Math = "math"
    Number = "number"
    Phone = "phone"
    Reference = "reference"
    Rollup = "rollup"
    RowID = "row_id"
    SingleValue = "single_value"
    SplitString = "split_string"
    String = "string"
    TextTemplate = "text_template"
    Time = "time"
    Uri = "uri"
    VideoUri = "video_uri"

class DataEditorTheme(Base):
    accent_color: Optional[str]
    accent_fg: Optional[str]
    accent_light: Optional[str]
    base_font_style: Optional[str]
    bg_bubble: Optional[str]
    bg_bubble_selected: Optional[str]
    bg_cell: Optional[str]
    bg_cell_medium: Optional[str]
    bg_header: Optional[str]
    bg_header_has_focus: Optional[str]
    bg_header_hovered: Optional[str]
    bg_icon_header: Optional[str]
    bg_search_result: Optional[str]
    border_color: Optional[str]
    cell_horizontal_padding: Optional[int]
    cell_vertical_padding: Optional[int]
    drilldown_border: Optional[str]
    editor_font_size: Optional[str]
    fg_icon_header: Optional[str]
    font_family: Optional[str]
    header_bottom_border_color: Optional[str]
    header_font_style: Optional[str]
    horizontal_border_color: Optional[str]
    line_height: Optional[int]
    link_color: Optional[str]
    text_bubble: Optional[str]
    text_dark: Optional[str]
    text_group_header: Optional[str]
    text_header: Optional[str]
    text_header_selected: Optional[str]
    text_light: Optional[str]
    text_medium: Optional[str]

class Bounds(TypedDict):
    x: int
    y: int
    width: int
    height: int

class CompatSelection(TypedDict):
    items: list

class Rectangle(TypedDict):
    x: int
    y: int
    width: int
    height: int

class GridSelectionCurrent(TypedDict):
    cell: tuple[int, int]
    range: Rectangle
    rangeStack: list[Rectangle]

class GridSelection(TypedDict):
    current: Optional[GridSelectionCurrent]
    columns: CompatSelection
    rows: CompatSelection

class GroupHeaderClickedEventArgs(TypedDict):
    kind: str
    group: str
    location: tuple[int, int]
    bounds: Bounds
    isEdge: bool
    shiftKey: bool
    ctrlKey: bool
    metaKey: bool
    isTouch: bool
    localEventX: int
    localEventY: int
    button: int
    buttons: int
    scrollEdge: tuple[int, int]

class GridCell(TypedDict):
    span: Optional[List[int]]

class GridColumn(TypedDict):
    title: str
    group: Optional[str]

class DataEditor(NoSSRComponent):
    def add_imports(self) -> ImportDict: ...
    def add_hooks(self) -> list[str]: ...
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        rows: Optional[Union[Var[int], int]] = None,
        columns: Optional[
            Union[List[Dict[str, Any]], Var[List[Dict[str, Any]]]]
        ] = None,
        data: Optional[Union[List[List[Any]], Var[List[List[Any]]]]] = None,
        get_cell_content: Optional[Union[Var[str], str]] = None,
        get_cells_for_selection: Optional[Union[Var[bool], bool]] = None,
        on_paste: Optional[Union[Var[bool], bool]] = None,
        draw_focus_ring: Optional[Union[Var[bool], bool]] = None,
        fixed_shadow_x: Optional[Union[Var[bool], bool]] = None,
        fixed_shadow_y: Optional[Union[Var[bool], bool]] = None,
        freeze_columns: Optional[Union[Var[int], int]] = None,
        group_header_height: Optional[Union[Var[int], int]] = None,
        header_height: Optional[Union[Var[int], int]] = None,
        max_column_auto_width: Optional[Union[Var[int], int]] = None,
        max_column_width: Optional[Union[Var[int], int]] = None,
        min_column_width: Optional[Union[Var[int], int]] = None,
        row_height: Optional[Union[Var[int], int]] = None,
        row_markers: Optional[
            Union[
                Literal["both", "checkbox", "clickable-number", "none", "number"],
                Var[Literal["both", "checkbox", "clickable-number", "none", "number"]],
            ]
        ] = None,
        row_marker_start_index: Optional[Union[Var[int], int]] = None,
        row_marker_width: Optional[Union[Var[int], int]] = None,
        smooth_scroll_x: Optional[Union[Var[bool], bool]] = None,
        smooth_scroll_y: Optional[Union[Var[bool], bool]] = None,
        vertical_border: Optional[Union[Var[bool], bool]] = None,
        column_select: Optional[
            Union[
                Literal["multi", "none", "single"],
                Var[Literal["multi", "none", "single"]],
            ]
        ] = None,
        prevent_diagonal_scrolling: Optional[Union[Var[bool], bool]] = None,
        overscroll_x: Optional[Union[Var[int], int]] = None,
        overscroll_y: Optional[Union[Var[int], int]] = None,
        scroll_offset_x: Optional[Union[Var[int], int]] = None,
        scroll_offset_y: Optional[Union[Var[int], int]] = None,
        theme: Optional[
            Union[DataEditorTheme, Dict, Var[Union[DataEditorTheme, Dict]]]
        ] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, Any]]] = None,
        on_blur: Optional[EventType[[], BASE_STATE]] = None,
        on_cell_activated: Optional[
            Union[EventType[[], BASE_STATE], EventType[[tuple[int, int]], BASE_STATE]]
        ] = None,
        on_cell_clicked: Optional[
            Union[EventType[[], BASE_STATE], EventType[[tuple[int, int]], BASE_STATE]]
        ] = None,
        on_cell_context_menu: Optional[
            Union[EventType[[], BASE_STATE], EventType[[tuple[int, int]], BASE_STATE]]
        ] = None,
        on_cell_edited: Optional[
            Union[
                EventType[[], BASE_STATE],
                EventType[[tuple[int, int]], BASE_STATE],
                EventType[[tuple[int, int], GridCell], BASE_STATE],
            ]
        ] = None,
        on_click: Optional[EventType[[], BASE_STATE]] = None,
        on_column_resize: Optional[
            Union[
                EventType[[], BASE_STATE],
                EventType[[GridColumn], BASE_STATE],
                EventType[[GridColumn, int], BASE_STATE],
            ]
        ] = None,
        on_context_menu: Optional[EventType[[], BASE_STATE]] = None,
        on_delete: Optional[
            Union[EventType[[], BASE_STATE], EventType[[GridSelection], BASE_STATE]]
        ] = None,
        on_double_click: Optional[EventType[[], BASE_STATE]] = None,
        on_finished_editing: Optional[
            Union[
                EventType[[], BASE_STATE],
                EventType[[Union[GridCell, None]], BASE_STATE],
                EventType[[Union[GridCell, None], tuple[int, int]], BASE_STATE],
            ]
        ] = None,
        on_focus: Optional[EventType[[], BASE_STATE]] = None,
        on_group_header_clicked: Optional[
            Union[
                EventType[[], BASE_STATE],
                EventType[[tuple[int, int]], BASE_STATE],
                EventType[[tuple[int, int], GridCell], BASE_STATE],
            ]
        ] = None,
        on_group_header_context_menu: Optional[
            Union[
                EventType[[], BASE_STATE],
                EventType[[int], BASE_STATE],
                EventType[[int, GroupHeaderClickedEventArgs], BASE_STATE],
            ]
        ] = None,
        on_group_header_renamed: Optional[
            Union[
                EventType[[], BASE_STATE],
                EventType[[str], BASE_STATE],
                EventType[[str, str], BASE_STATE],
            ]
        ] = None,
        on_header_clicked: Optional[
            Union[EventType[[], BASE_STATE], EventType[[tuple[int, int]], BASE_STATE]]
        ] = None,
        on_header_context_menu: Optional[
            Union[EventType[[], BASE_STATE], EventType[[tuple[int, int]], BASE_STATE]]
        ] = None,
        on_header_menu_click: Optional[
            Union[
                EventType[[], BASE_STATE],
                EventType[[int], BASE_STATE],
                EventType[[int, Rectangle], BASE_STATE],
            ]
        ] = None,
        on_item_hovered: Optional[
            Union[EventType[[], BASE_STATE], EventType[[tuple[int, int]], BASE_STATE]]
        ] = None,
        on_mount: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_down: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_enter: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_leave: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_move: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_out: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_over: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_up: Optional[EventType[[], BASE_STATE]] = None,
        on_row_appended: Optional[EventType[[], BASE_STATE]] = None,
        on_scroll: Optional[EventType[[], BASE_STATE]] = None,
        on_selection_cleared: Optional[EventType[[], BASE_STATE]] = None,
        on_unmount: Optional[EventType[[], BASE_STATE]] = None,
        **props,
    ) -> "DataEditor":
        """Create the DataEditor component.

        Args:
            *children: The children of the data editor.
            rows: Number of rows.
            columns: Headers of the columns for the data grid.
            data: The data.
            get_cell_content: The name of the callback used to find the data to display.
            get_cells_for_selection: Allow selection for copying.
            on_paste: Allow paste.
            draw_focus_ring: Controls the drawing of the focus ring.
            fixed_shadow_x: Enables or disables the overlay shadow when scrolling horizontally.
            fixed_shadow_y: Enables or disables the overlay shadow when scrolling vertically.
            freeze_columns: The number of columns which should remain in place when scrolling horizontally. Doesn't include rowMarkers.
            group_header_height: Controls the header of the group header row.
            header_height: Controls the height of the header row.
            max_column_auto_width: Additional header icons:  header_icons: Var[Any] # (TODO: must be a map of name: svg) #noqa: ERA001  The maximum width a column can be automatically sized to.
            max_column_width: The maximum width a column can be resized to.
            min_column_width: The minimum width a column can be resized to.
            row_height: Determins the height of each row.
            row_markers: Kind of row markers.
            row_marker_start_index: Changes the starting index for row markers.
            row_marker_width: Sets the width of row markers in pixels, if unset row markers will automatically size.
            smooth_scroll_x: Enable horizontal smooth scrolling.
            smooth_scroll_y: Enable vertical smooth scrolling.
            vertical_border: Controls the drawing of the left hand vertical border of a column. If set to a boolean value it controls all borders.
            column_select: Allow columns selections. ("none", "single", "multi")
            prevent_diagonal_scrolling: Prevent diagonal scrolling.
            overscroll_x: Allow to scroll past the limit of the actual content on the horizontal axis.
            overscroll_y: Allow to scroll past the limit of the actual content on the vertical axis.
            scroll_offset_x: Initial scroll offset on the horizontal axis.
            scroll_offset_y: Initial scroll offset on the vertical axis.
            theme: global theme
            on_cell_activated: Fired when a cell is activated.
            on_cell_clicked: Fired when a cell is clicked.
            on_cell_context_menu: Fired when a cell is right-clicked.
            on_cell_edited: Fired when a cell is edited.
            on_group_header_clicked: Fired when a group header is clicked.
            on_group_header_context_menu: Fired when a group header is right-clicked.
            on_group_header_renamed: Fired when a group header is renamed.
            on_header_clicked: Fired when a header is clicked.
            on_header_context_menu: Fired when a header is right-clicked.
            on_header_menu_click: Fired when a header menu item is clicked.
            on_item_hovered: Fired when an item is hovered.
            on_delete: Fired when a selection is deleted.
            on_finished_editing: Fired when editing is finished.
            on_row_appended: Fired when a row is appended.
            on_selection_cleared: Fired when the selection is cleared.
            on_column_resize: Fired when a column is resized.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the data editor.

        Raises:
            ValueError: invalid input.

        Returns:
            The DataEditor component.&
        """
        ...

@serializer
def serialize_dataeditortheme(theme: DataEditorTheme): ...

data_editor = DataEditor.create
data_editor_theme = DataEditorTheme

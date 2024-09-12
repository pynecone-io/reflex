"""Interactive components provided by @radix-ui/themes."""

from typing import List, Literal

from reflex.components.component import ComponentNamespace
from reflex.components.core.breakpoints import Responsive
from reflex.components.el import elements
from reflex.ivars.base import ImmutableVar

from ..base import (
    RadixThemesComponent,
)


class TableRoot(elements.Table, RadixThemesComponent):
    """A semantic table for presenting tabular data."""

    tag = "Table.Root"

    # The size of the table: "1" | "2" | "3"
    size: ImmutableVar[Responsive[Literal["1", "2", "3"]]]

    # The variant of the table
    variant: ImmutableVar[Literal["surface", "ghost"]]


class TableHeader(elements.Thead, RadixThemesComponent):
    """The header of the table defines column names and other non-data elements."""

    tag = "Table.Header"

    _invalid_children: List[str] = ["TableBody"]

    _valid_parents: List[str] = ["TableRoot"]


class TableRow(elements.Tr, RadixThemesComponent):
    """A row containing table cells."""

    tag = "Table.Row"

    # The alignment of the row
    align: ImmutableVar[Literal["start", "center", "end", "baseline"]]

    _invalid_children: List[str] = ["TableBody", "TableHeader", "TableRow"]


class TableColumnHeaderCell(elements.Th, RadixThemesComponent):
    """A table cell that is semantically treated as a column header."""

    tag = "Table.ColumnHeaderCell"

    # The justification of the column
    justify: ImmutableVar[Literal["start", "center", "end"]]

    _invalid_children: List[str] = [
        "TableBody",
        "TableHeader",
        "TableRow",
        "TableCell",
        "TableColumnHeaderCell",
        "TableRowHeaderCell",
    ]


class TableBody(elements.Tbody, RadixThemesComponent):
    """The body of the table contains the data rows."""

    tag = "Table.Body"

    _invalid_children: List[str] = [
        "TableHeader",
        "TableRowHeaderCell",
        "TableColumnHeaderCell",
        "TableCell",
    ]

    _valid_parents: List[str] = ["TableRoot"]


class TableCell(elements.Td, RadixThemesComponent):
    """A cell containing data."""

    tag = "Table.Cell"

    # The justification of the column
    justify: ImmutableVar[Literal["start", "center", "end"]]

    _invalid_children: List[str] = [
        "TableBody",
        "TableHeader",
        "TableRowHeaderCell",
        "TableColumnHeaderCell",
        "TableCell",
    ]


class TableRowHeaderCell(elements.Th, RadixThemesComponent):
    """A table cell that is semantically treated as a row header."""

    tag = "Table.RowHeaderCell"

    # The justification of the column
    justify: ImmutableVar[Literal["start", "center", "end"]]

    _invalid_children: List[str] = [
        "TableBody",
        "TableHeader",
        "TableRow",
        "TableCell",
        "TableColumnHeaderCell",
        "TableRowHeaderCell",
    ]


class Table(ComponentNamespace):
    """Table components namespace."""

    root = staticmethod(TableRoot.create)
    header = staticmethod(TableHeader.create)
    body = staticmethod(TableBody.create)
    row = staticmethod(TableRow.create)
    cell = staticmethod(TableCell.create)
    column_header_cell = staticmethod(TableColumnHeaderCell.create)
    row_header_cell = staticmethod(TableRowHeaderCell.create)


table = Table()

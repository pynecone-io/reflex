"""Table components."""

from typing import Any, List, Optional

from pynecone import utils
from pynecone.components.component import Component, ImportDict
from pynecone.components.tags import Tag
from pynecone.var import BaseVar, Var


class Gridjs(Component):
    """A component that wraps a nivo bar component."""

    library = "gridjs-react"


class DataTable(Gridjs):
    """A data table component."""

    tag = "Grid"

    # The data to display. Either a list of dictionaries or a pandas dataframe.
    data: Any

    # The columns to display.
    columns: Var[List]

    # Enable a search bar.
    search: Var[bool]

    # Enable sorting on columns.
    sort: Var[bool]

    # Enable resizable columns.
    resizable: Var[bool]

    # Enable pagination.
    pagination: Var[bool]

    @classmethod
    def get_alias(cls) -> Optional[str]:
        """Get the alias for the component.

        Returns:
            The alias.
        """
        return "DataTableGrid"

    @classmethod
    def create(cls, *children, **props):
        """Create a datatable component.

        Args:
            *children: The children of the component.
            **props: The props to pass to the component.

        Returns:
            The datatable component.

        Raises:
            ValueError: If a pandas dataframe is passed in and columns are also provided.
        """
        # If data is a pandas dataframe and columns are provided throw an error.
        if utils.is_dataframe(type(props.get("data"))) and props.get("columns"):
            raise ValueError(
                "Cannot pass in both a pandas dataframe and columns to the data_table component."
            )

        # If data is a list and columns are not provided, throw an error
        if (isinstance(data := props.get("data"), Var) and isinstance(data.type_, List) or isinstance(data, List)) and not props.get("columns"):
            raise ValueError(
                "column field should be specified when the data field is a list type"
            )

        # Create the component.
        return super().create(
            *children,
            **props,
        )

    def _get_imports(self) -> ImportDict:
        return utils.merge_imports(
            super()._get_imports(), {"": {"gridjs/dist/theme/mermaid.css"}}
        )

    def _render(self) -> Tag:
        # If given a var dataframe, get the data and columns
        if isinstance(self.data, Var):
            if utils.is_dataframe(self.data.type_):
                self.columns = BaseVar(
                    name=f"{self.data.name}.columns",
                    type_=List[Any],
                    state=self.data.state,
                )
                self.data = BaseVar(
                    name=f"{self.data.name}.data",
                    type_=List[List[Any]],
                    state=self.data.state,
                )
            else:
                self.columns = BaseVar(
                    name=f"{self.columns.name}",
                    type_=List[Any],
                    state=self.data.state,
                ) if self.columns else None
                self.data = BaseVar(
                    name=f"{self.data.name}",
                    type_=List[List[Any]],
                    state=self.data.state,
                )

        # If given a pandas df break up the data and columns
        if utils.is_dataframe(type(self.data)):
            self.columns = Var.create(list(self.data.columns.values.tolist()))  # type: ignore
            self.data = Var.create(utils.format_dataframe_values(self.data))  # type: ignore

        # Render the table.
        return super()._render()

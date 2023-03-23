"""A React tag."""

from __future__ import annotations

import json
import os
import re
from typing import TYPE_CHECKING, Any, Dict, Optional, Set, Tuple, Union

from plotly.graph_objects import Figure
from plotly.io import to_json

from pynecone.base import Base
from pynecone.event import EventChain
from pynecone.utils import format, types
from pynecone.var import Var
from pynecone.compiler import templates

if TYPE_CHECKING:
    from pynecone.components.component import ComponentStyle


class Tag(Base):
    """A React tag."""

    # The name of the tag.
    name: str = ""

    # The props of the tag.
    props: Dict[str, Any] = {}

    # The inner contents of the tag.
    contents: str = ""

    # Args to pass to the tag.
    args: Optional[Tuple[str, ...]] = None

    # Special props that aren't key value pairs.
    special_props: Set[Var] = set()

    def __init__(self, *args, **kwargs):
        """Initialize the tag.

        Args:
            *args: Args to initialize the tag.
            **kwargs: Kwargs to initialize the tag.
        """
        # Convert any props to vars.
        if "props" in kwargs:
            kwargs["props"] = {
                name: Var.create(value) for name, value in kwargs["props"].items()
            }
        super().__init__(*args, **kwargs)

    @staticmethod
    def format_prop(
        prop: Union[Var, EventChain, ComponentStyle, str],
    ) -> Union[int, float, str]:
        """Format a prop.

        Args:
            prop: The prop to format.

        Returns:
            The formatted prop to display within a tag.
        """
        # Handle var props.
        if isinstance(prop, Var):
            if not prop.is_local or prop.is_string:
                return str(prop)
            if issubclass(prop.type_, str):
                return format.json_dumps(prop.full_name)
            prop = prop.full_name

        # Handle event props.
        elif isinstance(prop, EventChain):
            local_args = ",".join(prop.events[0].local_args)

            if len(prop.events) == 1 and prop.events[0].upload:
                # Special case for upload events.
                event = format.format_upload_event(prop.events[0])
            else:
                # All other events.
                chain = ",".join([format.format_event(event) for event in prop.events])
                event = f"Event([{chain}])"
            prop = f"({local_args}) => {event}"

        # Handle other types.
        elif isinstance(prop, str):
            if format.is_wrapped(prop, "{"):
                return prop
            return format.json_dumps(prop)

        elif isinstance(prop, Figure):
            prop = json.loads(to_json(prop))["data"]  # type: ignore

        # For dictionaries, convert any properties to strings.
        else:
            if isinstance(prop, dict):
                # Convert any var keys to strings.
                prop = {
                    key: str(val) if isinstance(val, Var) else val
                    for key, val in prop.items()
                }

            # Dump the prop as JSON.
            prop = format.json_dumps(prop)

            # This substitution is necessary to unwrap var values.
            prop = re.sub('"{', "", prop)
            prop = re.sub('}"', "", prop)
            prop = re.sub('\\\\"', '"', prop)

        # Wrap the variable in braces.
        assert isinstance(prop, str), "The prop must be a string."
        return format.wrap(prop, "{", check_first=False)

    def format_props(self) -> list:
        """Format the tag's props.

        Returns:
            The formatted props.
        """
        # If there are no props, return an empty string.
        if len(self.props) == 0:
            return ""

        # Format all the props.
        return [
            f"{name}={self.format_prop(prop)}"
            for name, prop in sorted(self.props.items())
            if prop is not None
        ] + [
            str(prop) for prop in self.special_props
        ]

    def __str__(self) -> str:
        """Render the tag as a React string.

        Returns:
            The React code to render the tag.
        """
        props = self.format_props()

        if len(self.contents) == 0:
            # If there is no inner content, we don't need a closing tag.
            tag_str = templates.NO_CONTENT_TAG.render(tag_name=self.name, props=props)
        else:
            if self.args is not None:
                # If there are args, wrap the tag in a function call.
                args_str = ", ".join(self.args)
                contents = f"{{({{{args_str}}}) => ({self.contents})}}"
            else:
                contents = self.contents
            # Otherwise wrap it in opening and closing tags.
            open = templates.OPEN_TAG.render(tag_name=self.name, props=props)
            close = format.wrap(f"/{self.name}", "<")
            tag_str = format.wrap(contents, open, close)

        return tag_str

    def add_props(self, **kwargs: Optional[Any]) -> Tag:
        """Add props to the tag.

        Args:
            **kwargs: The props to add.

        Returns:
            The tag with the props added.
        """
        self.props.update(
            {
                format.to_camel_case(name): prop
                if types._isinstance(prop, Union[EventChain, dict])
                else Var.create(prop)
                for name, prop in kwargs.items()
                if self.is_valid_prop(prop)
            }
        )
        return self

    def remove_props(self, *args: str) -> Tag:
        """Remove props from the tag.

        Args:
            *args: The props to remove.

        Returns:
            The tag with the props removed.
        """
        for name in args:
            if name in self.props:
                del self.props[name]
        return self

    @staticmethod
    def is_valid_prop(prop: Optional[Var]) -> bool:
        """Check if the prop is valid.

        Args:
            prop: The prop to check.

        Returns:
            Whether the prop is valid.
        """
        return prop is not None and not (isinstance(prop, dict) and len(prop) == 0)

"""A highlight component."""

from typing import Dict, List

from reflex.components.chakra import ChakraComponent
from reflex.components.tags import Tag
from reflex.vars import Var


class Highlight(ChakraComponent):
    """Highlights a specific part of a string."""

    tag = "Highlight"

    # A query for the text to highlight. Can be a string or a list of strings.
    query: Var[List[str]]

    # The style of the content.
    # Note: styles and style are different prop.
    styles: Var[Dict] = {"px": "2", "py": "1", "rounded": "full", "bg": "teal.100"}  # type: ignore

    def _render_tag(self) -> Tag:
        return super()._render_tag().add_props(styles=self.style)

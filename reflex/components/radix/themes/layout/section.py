"""Declarative layout and common spacing props."""

from __future__ import annotations

from typing import Literal

from reflex.components.core.breakpoints import Responsive
from reflex.components.el import elements
from reflex.ivars.base import LiteralVar
from reflex.vars import Var

from ..base import RadixThemesComponent

LiteralSectionSize = Literal["1", "2", "3"]


class Section(elements.Section, RadixThemesComponent):
    """Denotes a section of page content."""

    tag = "Section"

    # The size of the section: "1" - "3" (default "2")
    size: Var[Responsive[LiteralSectionSize]] = LiteralVar.create("2")


section = Section.create

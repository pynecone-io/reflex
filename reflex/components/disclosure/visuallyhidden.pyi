"""Stub file for visuallyhidden.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, overload, Optional, Union
from reflex.components.libs.chakra import ChakraComponent
from reflex.vars import Var
from reflex.event import EventChain

class VisuallyHidden(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "VisuallyHidden": ...  # type: ignore

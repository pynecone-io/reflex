"""Stub file for spinner.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, overload, Optional, Union
from reflex.components.libs.chakra import ChakraComponent
from reflex.vars import Var
from reflex.event import EventChain

class Spinner(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, empty_color: Optional[Union[Var[str], str]] = None, label: Optional[Union[Var[str], str]] = None, speed: Optional[Union[Var[str], str]] = None, thickness: Optional[Union[Var[int], int]] = None, size: Optional[Union[Var[str], str]] = None, **props) -> "Spinner": ...  # type: ignore

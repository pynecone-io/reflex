"""Stub file for datatable.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import List, Dict, Any, Union, overload, Optional
from reflex.components.component import Component
from reflex.vars import Var
from reflex.event import EventChain

class Gridjs(Component):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "Gridjs": ...  # type: ignore

class DataTable(Gridjs):
    @overload
    @classmethod
    def create(cls, *children, data: Optional[Any] = None, columns: Optional[Union[Var[List], List]] = None, search: Optional[Union[Var[bool], bool]] = None, sort: Optional[Union[Var[bool], bool]] = None, resizable: Optional[Union[Var[bool], bool]] = None, pagination: Optional[Union[Var[Union[bool, Dict]], Union[bool, Dict]]] = None, **props) -> "DataTable": ...  # type: ignore

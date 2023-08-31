"""Stub file for markdown.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import List, Dict, Callable, Any, Union, overload, Optional
from reflex.components.component import Component
from reflex.vars import Var
from reflex.event import EventChain

components_by_tag: Dict[str, Callable]

class Markdown(Component):
    @overload
    @classmethod
    def create(cls, *children, custom_styles: Optional[Dict[str, Style]] = None, **props) -> "Markdown": ...  # type: ignore

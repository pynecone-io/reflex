"""Stub file for image.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Union, Set, overload, Optional
from reflex.components.libs.chakra import ChakraComponent
from reflex.vars import Var
from reflex.event import EventChain

class Image(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, align: Optional[Var[str]] = None, fallback: Optional[Component] = None, fallback_src: Optional[Var[str]] = None, fit: Optional[Var[str]] = None, html_height: Optional[Var[str]] = None, html_width: Optional[Var[str]] = None, ignore_fallback: Optional[Var[bool]] = None, loading: Optional[Var[str]] = None, src: Optional[Var[Any]] = None, alt: Optional[Var[str]] = None, src_set: Optional[Var[str]] = None, **props) -> "Image": ...  # type: ignore

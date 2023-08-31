"""Stub file for accordion.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Union, Optional, overload, Any, List
from reflex.components.libs.chakra import ChakraComponent
from reflex.vars import Var
from reflex.event import EventChain

class Accordion(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, items, icon_pos, allow_multiple: Optional[Union[Var[bool], bool]] = None, allow_toggle: Optional[Union[Var[bool], bool]] = None, default_index: Optional[Union[Var[Optional[List[int]]], Optional[List[int]]]] = None, index: Optional[Union[Var[Union[int, List[int]]], Union[int, List[int]]]] = None, reduce_motion: Optional[Union[Var[bool], bool]] = None, **props) -> "Accordion": ...  # type: ignore

class AccordionItem(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, id_: Optional[Union[Var[str], str]] = None, is_disabled: Optional[Union[Var[bool], bool]] = None, is_focusable: Optional[Union[Var[bool], bool]] = None, **props) -> "AccordionItem": ...  # type: ignore

class AccordionButton(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "AccordionButton": ...  # type: ignore

class AccordionPanel(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "AccordionPanel": ...  # type: ignore

class AccordionIcon(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "AccordionIcon": ...  # type: ignore

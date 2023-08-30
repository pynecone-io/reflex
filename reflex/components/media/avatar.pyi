"""Stub file for avatar.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import overload, Optional, Any, Union
from reflex.components.libs.chakra import ChakraComponent
from reflex.vars import Var

class Avatar(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, icon: Optional[Union[Var[str], str]] = None, icon_label: Optional[Union[Var[str], str]] = None, ignore_fallback: Optional[Union[Var[bool], bool]] = None, name: Optional[Union[Var[str], str]] = None, show_border: Optional[Union[Var[bool], bool]] = None, src: Optional[Union[Var[str], str]] = None, src_set: Optional[Union[Var[str], str]] = None, size: Optional[Union[Var[str], str]] = None, **props) -> "Avatar": ...  # type: ignore

class AvatarBadge(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "AvatarBadge": ...  # type: ignore

class AvatarGroup(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, max_: Optional[Union[Var[int], int]] = None, spacing: Optional[Union[Var[int], int]] = None, **props) -> "AvatarGroup": ...  # type: ignore

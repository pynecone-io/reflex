"""Stub file for audio.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, overload, Optional, Union
from reflex.components.libs.react_player import ReactPlayerComponent
from reflex.vars import Var
from reflex.event import EventChain

class Audio(ReactPlayerComponent):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "Audio": ...  # type: ignore

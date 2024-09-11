"""Define the base Reflex class."""

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, ClassVar, List, Optional, Type, Union

if TYPE_CHECKING:
    from reflex.utils.types import override
else:

    def override(fn):
        """Decorator to indicate that a method is meant to override a parent method.

        Args:
            fn: The method to override.

        Returns:
            The unmodified method.
        """
        return fn


try:
    if TYPE_CHECKING:
        from pydantic.v1.typing import AbstractSetIntStr, MappingIntStrAny
    import pydantic.v1.main as pydantic_main
    from pydantic.v1 import BaseModel
    from pydantic.v1.fields import ModelField

except ModuleNotFoundError:
    if TYPE_CHECKING:
        from pydantic.typing import AbstractSetIntStr, MappingIntStrAny
    else:
        import pydantic.main as pydantic_main
        from pydantic import BaseModel
        from pydantic.fields import ModelField  # type: ignore


from reflex import constants


def validate_field_name(bases: List[Type["BaseModel"]], field_name: str) -> None:
    """Ensure that the field's name does not shadow an existing attribute of the model.

    Args:
        bases: List of base models to check for shadowed attrs.
        field_name: name of attribute

    Raises:
        VarNameError: If state var field shadows another in its parent state
    """
    from reflex.utils.exceptions import VarNameError

    reload = os.getenv(constants.RELOAD_CONFIG) == "True"
    for base in bases:
        try:
            if not reload and getattr(base, field_name, None):
                pass
        except TypeError as te:
            raise VarNameError(
                f'State var "{field_name}" in {base} has been shadowed by a substate var; '
                f'use a different field name instead".'
            ) from te


# monkeypatch pydantic validate_field_name method to skip validating
# shadowed state vars when reloading app via utils.prerequisites.get_app(reload=True)
pydantic_main.validate_field_name = validate_field_name  # type: ignore


class UsedSerialization:
    """A mixin which allows tracking of fields used in the frontend.
    You can subclass this and add a @rx.serializer which uses the __used_fields__ attribute to only serialize used fields.
    Take a look at SlimBase for an example implementation.
    """

    __used_fields__: ClassVar[set[str]] = set()


class Base(BaseModel):  # pyright: ignore [reportUnboundVariable]
    """The base class subclassed by all Reflex classes.

    This class wraps Pydantic and provides common methods such as
    serialization and setting fields.

    Any data structure that needs to be transferred between the
    frontend and backend should subclass this class.
    """

    class Config:
        """Pydantic config."""

        arbitrary_types_allowed = True
        use_enum_values = True
        extra = "allow"

    def json(self) -> str:
        """Convert the object to a json string.

        Returns:
            The object as a json string.
        """
        from reflex.utils.serializers import serialize

        return self.__config__.json_dumps(  # type: ignore
            self.dict(),
            default=serialize,
        )

    def set(self, **kwargs):
        """Set multiple fields and return the object.

        Args:
            **kwargs: The fields and values to set.

        Returns:
            The object with the fields set.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)
        return self

    @classmethod
    def get_fields(cls) -> dict[str, Any]:
        """Get the fields of the object.

        Returns:
            The fields of the object.
        """
        return cls.__fields__

    @classmethod
    def add_field(cls, var: Any, default_value: Any):
        """Add a pydantic field after class definition.

        Used by State.add_var() to correctly handle the new variable.

        Args:
            var: The variable to add a pydantic field for.
            default_value: The default value of the field
        """
        var_name = var._var_name.split(".")[-1]
        new_field = ModelField.infer(
            name=var_name,
            value=default_value,
            annotation=var._var_type,
            class_validators=None,
            config=cls.__config__,  # type: ignore
        )
        cls.__fields__.update({var_name: new_field})

    def get_value(self, key: str) -> Any:
        """Get the value of a field.

        Args:
            key: The key of the field.

        Returns:
            The value of the field.
        """
        if isinstance(key, str) and key in self.__fields__:
            # Seems like this function signature was wrong all along?
            # If the user wants a field that we know of, get it and pass it off to _get_value
            key = getattr(self, key)
        return self._get_value(
            key,
            to_dict=True,
            by_alias=False,
            include=None,
            exclude=None,
            exclude_unset=False,
            exclude_defaults=False,
            exclude_none=False,
        )


class SlimBase(Base, UsedSerialization):
    """A slimmed down version of the Base class.
    Only used fields will be included in the dict for serialization.
    """

    @override
    def dict(
        self,
        *,
        include: Optional[Union[AbstractSetIntStr, MappingIntStrAny]] = None,
        exclude: Optional[Union[AbstractSetIntStr, MappingIntStrAny]] = None,
        by_alias: bool = False,
        skip_defaults: Optional[bool] = None,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
    ) -> dict[str, Any]:
        """Convert the object to a dict.

        We override the default dict method to only include fields that are used.

        Args:
            include: The fields to include.
            exclude: The fields to exclude.
            by_alias: Whether to use the alias names.
            skip_defaults: Whether to skip default values.
            exclude_unset: Whether to exclude unset values.
            exclude_defaults: Whether to exclude default values.
            exclude_none: Whether to exclude None values.

        Returns:
            The object as a dict.
        """
        if not include and isinstance(self, UsedSerialization):
            include = self.__used_fields__
        return super().dict(
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            skip_defaults=skip_defaults,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
        )

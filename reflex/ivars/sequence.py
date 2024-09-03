"""Collection of string classes and utilities."""

from __future__ import annotations

import dataclasses
import inspect
import json
import re
import sys
import typing
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Literal,
    Set,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)

from reflex import constants
from reflex.constants.base import REFLEX_VAR_OPENING_TAG
from reflex.utils.types import GenericType, get_origin
from reflex.vars import (
    ImmutableVarData,
    Var,
    VarData,
    _global_vars,
)

from .base import (
    CachedVarOperation,
    CustomVarOperationReturn,
    ImmutableVar,
    LiteralVar,
    cached_property_no_lock,
    figure_out_type,
    unionize,
    var_operation,
    var_operation_return,
)
from .number import (
    BooleanVar,
    LiteralNumberVar,
    NumberVar,
)

if TYPE_CHECKING:
    from .object import ObjectVar


class StringVar(ImmutableVar[str]):
    """Base class for immutable string vars."""

    def __add__(self, other: StringVar | str) -> ConcatVarOperation:
        """Concatenate two strings.

        Args:
            other: The other string.

        Returns:
            The string concatenation operation.
        """
        return ConcatVarOperation.create(self, other)

    def __radd__(self, other: StringVar | str) -> ConcatVarOperation:
        """Concatenate two strings.

        Args:
            other: The other string.

        Returns:
            The string concatenation operation.
        """
        return ConcatVarOperation.create(other, self)

    def __mul__(self, other: NumberVar | int) -> StringVar:
        """Multiply the sequence by a number or an integer.

        Args:
            other (NumberVar | int): The number or integer to multiply the sequence by.

        Returns:
            StringVar: The resulting sequence after multiplication.
        """
        return (self.split() * other).join()

    def __rmul__(self, other: NumberVar | int) -> StringVar:
        """Multiply the sequence by a number or an integer.

        Args:
            other (NumberVar | int): The number or integer to multiply the sequence by.

        Returns:
            StringVar: The resulting sequence after multiplication.
        """
        return (self.split() * other).join()

    def __getitem__(self, i: slice | int | NumberVar) -> StringVar:
        """Get a slice of the string.

        Args:
            i: The slice.

        Returns:
            The string slice operation.
        """
        if isinstance(i, slice):
            return self.split()[i].join()
        return string_item_operation(self, i)

    def length(self) -> NumberVar:
        """Get the length of the string.

        Returns:
            The string length operation.
        """
        return self.split().length()

    def lower(self) -> StringVar:
        """Convert the string to lowercase.

        Returns:
            The string lower operation.
        """
        return string_lower_operation(self)

    def upper(self) -> StringVar:
        """Convert the string to uppercase.

        Returns:
            The string upper operation.
        """
        return string_upper_operation(self)

    def strip(self) -> StringVar:
        """Strip the string.

        Returns:
            The string strip operation.
        """
        return string_strip_operation(self)

    def bool(self):
        """Boolean conversion.

        Returns:
            The boolean value of the string.
        """
        return self.length() != 0

    def reversed(self) -> StringVar:
        """Reverse the string.

        Returns:
            The string reverse operation.
        """
        return self.split().reverse().join()

    def contains(self, other: StringVar | str) -> BooleanVar:
        """Check if the string contains another string.

        Args:
            other: The other string.

        Returns:
            The string contains operation.
        """
        return string_contains_operation(self, other)

    def split(self, separator: StringVar | str = "") -> ArrayVar[List[str]]:
        """Split the string.

        Args:
            separator: The separator.

        Returns:
            The string split operation.
        """
        return string_split_operation(self, separator)

    def startswith(self, prefix: StringVar | str) -> BooleanVar:
        """Check if the string starts with a prefix.

        Args:
            prefix: The prefix.

        Returns:
            The string starts with operation.
        """
        return string_starts_with_operation(self, prefix)


@var_operation
def string_lower_operation(string: StringVar):
    """Convert a string to lowercase.

    Args:
        string: The string to convert.

    Returns:
        The lowercase string.
    """
    return var_operation_return(js_expression=f"{string}.toLowerCase()", var_type=str)


@var_operation
def string_upper_operation(string: StringVar):
    """Convert a string to uppercase.

    Args:
        string: The string to convert.

    Returns:
        The uppercase string.
    """
    return var_operation_return(js_expression=f"{string}.toUpperCase()", var_type=str)


@var_operation
def string_strip_operation(string: StringVar):
    """Strip a string.

    Args:
        string: The string to strip.

    Returns:
        The stripped string.
    """
    return var_operation_return(js_expression=f"{string}.trim()", var_type=str)


@var_operation
def string_contains_operation(haystack: StringVar, needle: StringVar | str):
    """Check if a string contains another string.

    Args:
        haystack: The haystack.
        needle: The needle.

    Returns:
        The string contains operation.
    """
    return var_operation_return(
        js_expression=f"{haystack}.includes({needle})", var_type=bool
    )


@var_operation
def string_starts_with_operation(full_string: StringVar, prefix: StringVar | str):
    """Check if a string starts with a prefix.

    Args:
        full_string: The full string.
        prefix: The prefix.

    Returns:
        Whether the string starts with the prefix.
    """
    return var_operation_return(
        js_expression=f"{full_string}.startsWith({prefix})", var_type=bool
    )


@var_operation
def string_item_operation(string: StringVar, index: NumberVar | int):
    """Get an item from a string.

    Args:
        string: The string.
        index: The index of the item.

    Returns:
        The item from the string.
    """
    return var_operation_return(js_expression=f"{string}.at({index})", var_type=str)


@var_operation
def array_join_operation(array: ArrayVar, sep: StringVar | str = ""):
    """Join the elements of an array.

    Args:
        array: The array.
        sep: The separator.

    Returns:
        The joined elements.
    """
    return var_operation_return(js_expression=f"{array}.join({sep})", var_type=str)


# Compile regex for finding reflex var tags.
_decode_var_pattern_re = (
    rf"{constants.REFLEX_VAR_OPENING_TAG}(.*?){constants.REFLEX_VAR_CLOSING_TAG}"
)
_decode_var_pattern = re.compile(_decode_var_pattern_re, flags=re.DOTALL)


@dataclasses.dataclass(
    eq=False,
    frozen=True,
    **{"slots": True} if sys.version_info >= (3, 10) else {},
)
class LiteralStringVar(LiteralVar, StringVar):
    """Base class for immutable literal string vars."""

    _var_value: str = dataclasses.field(default="")

    @classmethod
    def create(
        cls,
        value: str,
        _var_data: VarData | None = None,
    ) -> LiteralStringVar | ConcatVarOperation:
        """Create a var from a string value.

        Args:
            value: The value to create the var from.
            _var_data: Additional hooks and imports associated with the Var.

        Returns:
            The var.
        """
        if REFLEX_VAR_OPENING_TAG in value:
            strings_and_vals: list[Var | str] = []
            offset = 0

            # Initialize some methods for reading json.
            var_data_config = VarData().__config__

            def json_loads(s):
                try:
                    return var_data_config.json_loads(s)
                except json.decoder.JSONDecodeError:
                    return var_data_config.json_loads(
                        var_data_config.json_loads(f'"{s}"')
                    )

            # Find all tags
            while m := _decode_var_pattern.search(value):
                start, end = m.span()

                strings_and_vals.append(value[:start])

                serialized_data = m.group(1)

                if serialized_data.isnumeric() or (
                    serialized_data[0] == "-" and serialized_data[1:].isnumeric()
                ):
                    # This is a global immutable var.
                    var = _global_vars[int(serialized_data)]
                    strings_and_vals.append(var)
                    value = value[(end + len(var._var_name)) :]
                else:
                    data = json_loads(serialized_data)
                    string_length = data.pop("string_length", None)
                    var_data = VarData.parse_obj(data)

                    # Use string length to compute positions of interpolations.
                    if string_length is not None:
                        realstart = start + offset
                        var_data.interpolations = [
                            (realstart, realstart + string_length)
                        ]
                        var_content = value[end : (end + string_length)]
                        if (
                            var_content[0] == "{"
                            and var_content[-1] == "}"
                            and strings_and_vals
                            and strings_and_vals[-1][-1] == "$"
                        ):
                            strings_and_vals[-1] = strings_and_vals[-1][:-1]
                            var_content = "(" + var_content[1:-1] + ")"
                        strings_and_vals.append(
                            ImmutableVar.create_safe(var_content, _var_data=var_data)
                        )
                        value = value[(end + string_length) :]

                offset += end - start

            strings_and_vals.append(value)

            filtered_strings_and_vals = [
                s for s in strings_and_vals if isinstance(s, Var) or s
            ]

            if len(filtered_strings_and_vals) == 1:
                return filtered_strings_and_vals[0].to(StringVar)  # type: ignore

            return ConcatVarOperation.create(
                *filtered_strings_and_vals,
                _var_data=_var_data,
            )

        return LiteralStringVar(
            _var_name=json.dumps(value),
            _var_type=str,
            _var_data=ImmutableVarData.merge(_var_data),
            _var_value=value,
        )

    def __hash__(self) -> int:
        """Get the hash of the var.

        Returns:
            The hash of the var.
        """
        return hash((self.__class__.__name__, self._var_value))

    def json(self) -> str:
        """Get the JSON representation of the var.

        Returns:
            The JSON representation of the var.
        """
        return json.dumps(self._var_value)


@dataclasses.dataclass(
    eq=False,
    frozen=True,
    **{"slots": True} if sys.version_info >= (3, 10) else {},
)
class ConcatVarOperation(CachedVarOperation, StringVar):
    """Representing a concatenation of literal string vars."""

    _var_value: Tuple[Var, ...] = dataclasses.field(default_factory=tuple)

    @cached_property_no_lock
    def _cached_var_name(self) -> str:
        """The name of the var.

        Returns:
            The name of the var.
        """
        list_of_strs: List[Union[str, Var]] = []
        last_string = ""
        for var in self._var_value:
            if isinstance(var, LiteralStringVar):
                last_string += var._var_value
            else:
                if last_string:
                    list_of_strs.append(last_string)
                    last_string = ""
                list_of_strs.append(var)

        if last_string:
            list_of_strs.append(last_string)

        list_of_strs_filtered = [
            str(LiteralVar.create(s)) for s in list_of_strs if isinstance(s, Var) or s
        ]

        if len(list_of_strs_filtered) == 1:
            return list_of_strs_filtered[0]

        return "(" + "+".join(list_of_strs_filtered) + ")"

    @cached_property_no_lock
    def _cached_get_all_var_data(self) -> ImmutableVarData | None:
        """Get all the VarData associated with the Var.

        Returns:
            The VarData associated with the Var.
        """
        return ImmutableVarData.merge(
            *[
                var._get_all_var_data()
                for var in self._var_value
                if isinstance(var, Var)
            ],
            self._var_data,
        )

    @classmethod
    def create(
        cls,
        *value: Var | str,
        _var_data: VarData | None = None,
    ) -> ConcatVarOperation:
        """Create a var from a string value.

        Args:
            value: The values to concatenate.
            _var_data: Additional hooks and imports associated with the Var.

        Returns:
            The var.
        """
        return cls(
            _var_name="",
            _var_type=str,
            _var_data=ImmutableVarData.merge(_var_data),
            _var_value=tuple(map(LiteralVar.create, value)),
        )


ARRAY_VAR_TYPE = TypeVar("ARRAY_VAR_TYPE", bound=Union[List, Tuple, Set])

OTHER_TUPLE = TypeVar("OTHER_TUPLE")

INNER_ARRAY_VAR = TypeVar("INNER_ARRAY_VAR")

KEY_TYPE = TypeVar("KEY_TYPE")
VALUE_TYPE = TypeVar("VALUE_TYPE")


class ArrayVar(ImmutableVar[ARRAY_VAR_TYPE]):
    """Base class for immutable array vars."""

    def join(self, sep: StringVar | str = "") -> StringVar:
        """Join the elements of the array.

        Args:
            sep: The separator between elements.

        Returns:
            The joined elements.
        """
        return array_join_operation(self, sep)

    def reverse(self) -> ArrayVar[ARRAY_VAR_TYPE]:
        """Reverse the array.

        Returns:
            The reversed array.
        """
        return array_reverse_operation(self)

    def __add__(self, other: ArrayVar[ARRAY_VAR_TYPE]) -> ArrayVar[ARRAY_VAR_TYPE]:
        """Concatenate two arrays.

        Parameters:
            other (ArrayVar[ARRAY_VAR_TYPE]): The other array to concatenate.

        Returns:
            ArrayConcatOperation: The concatenation of the two arrays.
        """
        return array_concat_operation(self, other)

    @overload
    def __getitem__(self, i: slice) -> ArrayVar[ARRAY_VAR_TYPE]: ...

    @overload
    def __getitem__(
        self: (
            ArrayVar[Tuple[int, OTHER_TUPLE]]
            | ArrayVar[Tuple[float, OTHER_TUPLE]]
            | ArrayVar[Tuple[int | float, OTHER_TUPLE]]
        ),
        i: Literal[0, -2],
    ) -> NumberVar: ...

    @overload
    def __getitem__(
        self: (
            ArrayVar[Tuple[OTHER_TUPLE, int]]
            | ArrayVar[Tuple[OTHER_TUPLE, float]]
            | ArrayVar[Tuple[OTHER_TUPLE, int | float]]
        ),
        i: Literal[1, -1],
    ) -> NumberVar: ...

    @overload
    def __getitem__(
        self: ArrayVar[Tuple[str, OTHER_TUPLE]], i: Literal[0, -2]
    ) -> StringVar: ...

    @overload
    def __getitem__(
        self: ArrayVar[Tuple[OTHER_TUPLE, str]], i: Literal[1, -1]
    ) -> StringVar: ...

    @overload
    def __getitem__(
        self: ArrayVar[Tuple[bool, OTHER_TUPLE]], i: Literal[0, -2]
    ) -> BooleanVar: ...

    @overload
    def __getitem__(
        self: ArrayVar[Tuple[OTHER_TUPLE, bool]], i: Literal[1, -1]
    ) -> BooleanVar: ...

    @overload
    def __getitem__(
        self: (
            ARRAY_VAR_OF_LIST_ELEMENT[int]
            | ARRAY_VAR_OF_LIST_ELEMENT[float]
            | ARRAY_VAR_OF_LIST_ELEMENT[int | float]
        ),
        i: int | NumberVar,
    ) -> NumberVar: ...

    @overload
    def __getitem__(
        self: ARRAY_VAR_OF_LIST_ELEMENT[str], i: int | NumberVar
    ) -> StringVar: ...

    @overload
    def __getitem__(
        self: ARRAY_VAR_OF_LIST_ELEMENT[bool], i: int | NumberVar
    ) -> BooleanVar: ...

    @overload
    def __getitem__(
        self: ARRAY_VAR_OF_LIST_ELEMENT[List[INNER_ARRAY_VAR]],
        i: int | NumberVar,
    ) -> ArrayVar[List[INNER_ARRAY_VAR]]: ...

    @overload
    def __getitem__(
        self: ARRAY_VAR_OF_LIST_ELEMENT[Set[INNER_ARRAY_VAR]],
        i: int | NumberVar,
    ) -> ArrayVar[Set[INNER_ARRAY_VAR]]: ...

    @overload
    def __getitem__(
        self: ARRAY_VAR_OF_LIST_ELEMENT[Tuple[INNER_ARRAY_VAR, ...]],
        i: int | NumberVar,
    ) -> ArrayVar[Tuple[INNER_ARRAY_VAR, ...]]: ...

    @overload
    def __getitem__(
        self: ARRAY_VAR_OF_LIST_ELEMENT[Dict[KEY_TYPE, VALUE_TYPE]],
        i: int | NumberVar,
    ) -> ObjectVar[Dict[KEY_TYPE, VALUE_TYPE]]: ...

    @overload
    def __getitem__(self, i: int | NumberVar) -> ImmutableVar: ...

    def __getitem__(
        self, i: slice | int | NumberVar
    ) -> ArrayVar[ARRAY_VAR_TYPE] | ImmutableVar:
        """Get a slice of the array.

        Args:
            i: The slice.

        Returns:
            The array slice operation.
        """
        if isinstance(i, slice):
            return ArraySliceOperation.create(self, i)
        return array_item_operation(self, i)

    def length(self) -> NumberVar:
        """Get the length of the array.

        Returns:
            The length of the array.
        """
        return array_length_operation(self)

    @overload
    @classmethod
    def range(cls, stop: int | NumberVar, /) -> ArrayVar[List[int]]: ...

    @overload
    @classmethod
    def range(
        cls,
        start: int | NumberVar,
        end: int | NumberVar,
        step: int | NumberVar = 1,
        /,
    ) -> ArrayVar[List[int]]: ...

    @classmethod
    def range(
        cls,
        first_endpoint: int | NumberVar,
        second_endpoint: int | NumberVar | None = None,
        step: int | NumberVar | None = None,
    ) -> ArrayVar[List[int]]:
        """Create a range of numbers.

        Args:
            first_endpoint: The end of the range if second_endpoint is not provided, otherwise the start of the range.
            second_endpoint: The end of the range.
            step: The step of the range.

        Returns:
            The range of numbers.
        """
        if second_endpoint is None:
            start = 0
            end = first_endpoint
        else:
            start = first_endpoint
            end = second_endpoint

        return array_range_operation(start, end, step or 1)

    def contains(self, other: Any) -> BooleanVar:
        """Check if the array contains an element.

        Args:
            other: The element to check for.

        Returns:
            The array contains operation.
        """
        return array_contains_operation(self, other)

    def __mul__(self, other: NumberVar | int) -> ArrayVar[ARRAY_VAR_TYPE]:
        """Multiply the sequence by a number or integer.

        Parameters:
            other (NumberVar | int): The number or integer to multiply the sequence by.

        Returns:
            ArrayVar[ARRAY_VAR_TYPE]: The result of multiplying the sequence by the given number or integer.
        """
        return repeat_array_operation(self, other)

    __rmul__ = __mul__  # type: ignore


LIST_ELEMENT = TypeVar("LIST_ELEMENT")

ARRAY_VAR_OF_LIST_ELEMENT = Union[
    ArrayVar[List[LIST_ELEMENT]],
    ArrayVar[Set[LIST_ELEMENT]],
    ArrayVar[Tuple[LIST_ELEMENT, ...]],
]


@dataclasses.dataclass(
    eq=False,
    frozen=True,
    **{"slots": True} if sys.version_info >= (3, 10) else {},
)
class LiteralArrayVar(CachedVarOperation, LiteralVar, ArrayVar[ARRAY_VAR_TYPE]):
    """Base class for immutable literal array vars."""

    _var_value: Union[
        List[Union[Var, Any]], Set[Union[Var, Any]], Tuple[Union[Var, Any], ...]
    ] = dataclasses.field(default_factory=list)

    @cached_property_no_lock
    def _cached_var_name(self) -> str:
        """The name of the var.

        Returns:
            The name of the var.
        """
        return (
            "["
            + ", ".join(
                [str(LiteralVar.create(element)) for element in self._var_value]
            )
            + "]"
        )

    @cached_property_no_lock
    def _cached_get_all_var_data(self) -> ImmutableVarData | None:
        """Get all the VarData associated with the Var.

        Returns:
            The VarData associated with the Var.
        """
        return ImmutableVarData.merge(
            *[
                LiteralVar.create(element)._get_all_var_data()
                for element in self._var_value
            ],
            self._var_data,
        )

    def __hash__(self) -> int:
        """Get the hash of the var.

        Returns:
            The hash of the var.
        """
        return hash((self.__class__.__name__, self._var_name))

    def json(self) -> str:
        """Get the JSON representation of the var.

        Returns:
            The JSON representation of the var.
        """
        return (
            "["
            + ", ".join(
                [LiteralVar.create(element).json() for element in self._var_value]
            )
            + "]"
        )

    @classmethod
    def create(
        cls,
        value: ARRAY_VAR_TYPE,
        _var_type: Type[ARRAY_VAR_TYPE] | None = None,
        _var_data: VarData | None = None,
    ) -> LiteralArrayVar[ARRAY_VAR_TYPE]:
        """Create a var from a string value.

        Args:
            value: The value to create the var from.
            _var_data: Additional hooks and imports associated with the Var.

        Returns:
            The var.
        """
        return cls(
            _var_name="",
            _var_type=figure_out_type(value) if _var_type is None else _var_type,
            _var_data=ImmutableVarData.merge(_var_data),
            _var_value=value,
        )


@var_operation
def string_split_operation(string: StringVar, sep: StringVar | str = ""):
    """Split a string.

    Args:
        string: The string to split.
        sep: The separator.

    Returns:
        The split string.
    """
    return var_operation_return(
        js_expression=f"{string}.split({sep})", var_type=List[str]
    )


@dataclasses.dataclass(
    eq=False,
    frozen=True,
    **{"slots": True} if sys.version_info >= (3, 10) else {},
)
class ArraySliceOperation(CachedVarOperation, ArrayVar):
    """Base class for immutable string vars that are the result of a string slice operation."""

    _array: ArrayVar = dataclasses.field(
        default_factory=lambda: LiteralArrayVar.create([])
    )
    _start: NumberVar | int = dataclasses.field(default_factory=lambda: 0)
    _stop: NumberVar | int = dataclasses.field(default_factory=lambda: 0)
    _step: NumberVar | int = dataclasses.field(default_factory=lambda: 1)

    @cached_property_no_lock
    def _cached_var_name(self) -> str:
        """The name of the var.

        Returns:
            The name of the var.

        Raises:
            ValueError: If the slice step is zero.
        """
        start, end, step = self._start, self._stop, self._step

        normalized_start = (
            LiteralVar.create(start)
            if start is not None
            else ImmutableVar.create_safe("undefined")
        )
        normalized_end = (
            LiteralVar.create(end)
            if end is not None
            else ImmutableVar.create_safe("undefined")
        )
        if step is None:
            return f"{str(self._array)}.slice({str(normalized_start)}, {str(normalized_end)})"
        if not isinstance(step, Var):
            if step < 0:
                actual_start = end + 1 if end is not None else 0
                actual_end = start + 1 if start is not None else self._array.length()
                return str(self._array[actual_start:actual_end].reverse()[::-step])
            if step == 0:
                raise ValueError("slice step cannot be zero")
            return f"{str(self._array)}.slice({str(normalized_start)}, {str(normalized_end)}).filter((_, i) => i % {str(step)} === 0)"

        actual_start_reverse = end + 1 if end is not None else 0
        actual_end_reverse = start + 1 if start is not None else self._array.length()

        return f"{str(self.step)} > 0 ? {str(self._array)}.slice({str(normalized_start)}, {str(normalized_end)}).filter((_, i) => i % {str(step)} === 0) : {str(self._array)}.slice({str(actual_start_reverse)}, {str(actual_end_reverse)}).reverse().filter((_, i) => i % {str(-step)} === 0)"

    @classmethod
    def create(
        cls,
        array: ArrayVar,
        slice: slice,
        _var_data: VarData | None = None,
    ) -> ArraySliceOperation:
        """Create a var from a string value.

        Args:
            array: The array.
            slice: The slice.
            _var_data: Additional hooks and imports associated with the Var.

        Returns:
            The var.
        """
        return cls(
            _var_name="",
            _var_type=array._var_type,
            _var_data=ImmutableVarData.merge(_var_data),
            _array=array,
            _start=slice.start,
            _stop=slice.stop,
            _step=slice.step,
        )


@var_operation
def array_reverse_operation(
    array: ArrayVar[ARRAY_VAR_TYPE],
) -> CustomVarOperationReturn[ARRAY_VAR_TYPE]:
    """Reverse an array.

    Args:
        array: The array to reverse.

    Returns:
        The reversed array.
    """
    return var_operation_return(
        js_expression=f"{array}.slice().reverse()",
        var_type=array._var_type,
    )


@var_operation
def array_length_operation(array: ArrayVar):
    """Get the length of an array.

    Args:
        array: The array.

    Returns:
        The length of the array.
    """
    return var_operation_return(
        js_expression=f"{array}.length",
        var_type=int,
    )


def is_tuple_type(t: GenericType) -> bool:
    """Check if a type is a tuple type.

    Args:
        t: The type to check.

    Returns:
        Whether the type is a tuple type.
    """
    if inspect.isclass(t):
        return issubclass(t, tuple)
    return get_origin(t) is tuple


@var_operation
def array_item_operation(array: ArrayVar, index: NumberVar | int):
    """Get an item from an array.

    Args:
        array: The array.
        index: The index of the item.

    Returns:
        The item from the array.
    """
    args = typing.get_args(array._var_type)
    if args and isinstance(index, LiteralNumberVar) and is_tuple_type(array._var_type):
        index_value = int(index._var_value)
        element_type = args[index_value % len(args)]
    else:
        element_type = unionize(*args)

    return var_operation_return(
        js_expression=f"{str(array)}.at({str(index)})",
        var_type=element_type,
    )


@var_operation
def array_range_operation(
    start: NumberVar | int, stop: NumberVar | int, step: NumberVar | int
):
    """Create a range of numbers.

    Args:
        start: The start of the range.
        stop: The end of the range.
        step: The step of the range.

    Returns:
        The range of numbers.
    """
    return var_operation_return(
        js_expression=f"Array.from({{ length: ({str(stop)} - {str(start)}) / {str(step)} }}, (_, i) => {str(start)} + i * {str(step)})",
        var_type=List[int],
    )


@var_operation
def array_contains_operation(haystack: ArrayVar, needle: Any | Var):
    """Check if an array contains an element.

    Args:
        haystack: The array to check.
        needle: The element to check for.

    Returns:
        The array contains operation.
    """
    return var_operation_return(
        js_expression=f"{haystack}.includes({needle})",
        var_type=bool,
    )


@dataclasses.dataclass(
    eq=False,
    frozen=True,
    **{"slots": True} if sys.version_info >= (3, 10) else {},
)
class ToStringOperation(CachedVarOperation, StringVar):
    """Base class for immutable string vars that are the result of a to string operation."""

    _original_var: Var = dataclasses.field(
        default_factory=lambda: LiteralStringVar.create("")
    )

    @cached_property_no_lock
    def _cached_var_name(self) -> str:
        """The name of the var.

        Returns:
            The name of the var.
        """
        return str(self._original_var)

    @classmethod
    def create(
        cls,
        original_var: Var,
        _var_data: VarData | None = None,
    ) -> ToStringOperation:
        """Create a var from a string value.

        Args:
            original_var: The original var.
            _var_data: Additional hooks and imports associated with the Var.

        Returns:
            The var.
        """
        return cls(
            _var_name="",
            _var_type=str,
            _var_data=ImmutableVarData.merge(_var_data),
            _original_var=original_var,
        )


@dataclasses.dataclass(
    eq=False,
    frozen=True,
    **{"slots": True} if sys.version_info >= (3, 10) else {},
)
class ToArrayOperation(CachedVarOperation, ArrayVar):
    """Base class for immutable array vars that are the result of a to array operation."""

    _original_var: Var = dataclasses.field(
        default_factory=lambda: LiteralArrayVar.create([])
    )

    @cached_property_no_lock
    def _cached_var_name(self) -> str:
        """The name of the var.

        Returns:
            The name of the var.
        """
        return str(self._original_var)

    @classmethod
    def create(
        cls,
        original_var: Var,
        _var_type: type[list] | type[set] | type[tuple] | None = None,
        _var_data: VarData | None = None,
    ) -> ToArrayOperation:
        """Create a var from a string value.

        Args:
            original_var: The original var.
            _var_data: Additional hooks and imports associated with the Var.

        Returns:
            The var.
        """
        return cls(
            _var_name="",
            _var_type=list if _var_type is None else _var_type,
            _var_data=ImmutableVarData.merge(_var_data),
            _original_var=original_var,
        )


@var_operation
def repeat_array_operation(
    array: ArrayVar[ARRAY_VAR_TYPE], count: NumberVar | int
) -> CustomVarOperationReturn[ARRAY_VAR_TYPE]:
    """Repeat an array a number of times.

    Args:
        array: The array to repeat.
        count: The number of times to repeat the array.

    Returns:
        The repeated array.
    """
    return var_operation_return(
        js_expression=f"Array.from({{ length: {count} }}).flatMap(() => {array})",
        var_type=array._var_type,
    )


@var_operation
def array_concat_operation(
    lhs: ArrayVar[ARRAY_VAR_TYPE], rhs: ArrayVar[ARRAY_VAR_TYPE]
) -> CustomVarOperationReturn[ARRAY_VAR_TYPE]:
    """Concatenate two arrays.

    Args:
        lhs: The left-hand side array.
        rhs: The right-hand side array.

    Returns:
        The concatenated array.
    """
    return var_operation_return(
        js_expression=f"[...{lhs}, ...{rhs}]",
        var_type=Union[lhs._var_type, rhs._var_type],
    )

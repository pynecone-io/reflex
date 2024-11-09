"""The base for CustomBackendServer."""

from __future__ import annotations

import os
from abc import abstractmethod
from dataclasses import Field, dataclass
from dataclasses import field as dc_field
from pathlib import Path
from typing import Any, Callable, Sequence

from reflex import constants
from reflex.constants.base import Env, LogLevel

ReturnCliTypeFn = Callable[[Any], str]


class CliType:
    """Cli type transformer."""

    @staticmethod
    def default(fmt: str) -> ReturnCliTypeFn:
        """Default cli transformer.

        Example:
            fmt: `'--env-file {value}'`
            value: `'/config.conf'`
            result => `'--env-file /config.conf'`
        """

        def wrapper(value: bool) -> str:
            return fmt.format(value=value)

        return wrapper

    @staticmethod
    def boolean(fmt: str, bool_value: bool = True) -> ReturnCliTypeFn:
        """When cli mode args only show when we want to activate it.

        Example:
            fmt: `'--reload'`
            value: `False`
            result => `''`

        Example:
            fmt: `'--reload'`
            value: `True`
            result => `'--reload'`
        """

        def wrapper(value: bool) -> str:
            return fmt if value is bool_value else ""

        return wrapper

    @staticmethod
    def boolean_toggle(
        fmt: str,
        toggle_kw: str = "no",
        toggle_sep: str = "-",
        toggle_value: bool = False,
        **kwargs,
    ) -> ReturnCliTypeFn:
        """When the cli mode is a boolean toggle `--access-log`/`--no-access-log`.

        Example:
            fmt: `'--{toggle_kw}{toggle_sep}access-log'`
            value: `False`
            toggle_value: `False` (default)
            result => `'--no-access-log'`

        Example:
            fmt: `'--{toggle_kw}{toggle_sep}access-log'`
            value: `True`
            toggle_value: `False` (default)
            result => `'--access-log'`

        Example:
            fmt: `'--{toggle_kw}{toggle_sep}access-log'`
            value: `True`
            toggle_value: `True`
            result => `'--no-access-log'`
        """

        def wrapper(value: bool) -> str:
            return fmt.format(
                **kwargs,
                toggle_kw=(toggle_kw if value is toggle_value else ""),
                toggle_sep=(toggle_sep if value is toggle_value else ""),
            )

        return wrapper

    @staticmethod
    def multiple(
        fmt: str,
        join_sep: str | None = None,
        value_transformer: Callable[[Any], str] = lambda value: str(value),
    ) -> ReturnCliTypeFn:
        r"""When the cli mode need multiple args or single args from an sequence.

        Example (Multiple args mode):
            fmt: `'--header {value}'`.
            data_list: `['X-Forwarded-Proto=https', 'X-Forwarded-For=0.0.0.0']`
            result => `'--header \"X-Forwarded-Proto=https\" --header \"X-Forwarded-For=0.0.0.0\"'`

        Example (Single args mode):
            fmt: `--headers {values}`
            data_list: `['X-Forwarded-Proto=https', 'X-Forwarded-For=0.0.0.0']`
            join_sep (required): `';'`
            result => `--headers \"X-Forwarded-Proto=https;X-Forwarded-For=0.0.0.0\"`

        Example (Single args mode):
            fmt: `--headers {values}`
            data_list: `[('X-Forwarded-Proto', 'https'), ('X-Forwarded-For', '0.0.0.0')]`
            join_sep (required): `';'`
            value_transformer: `lambda value: f'{value[0]}:{value[1]}'`
            result => `--headers \"X-Forwarded-Proto:https;X-Forwarded-For:0.0.0.0\"`
        """

        def wrapper(values: Sequence[str]) -> str:
            return (
                fmt.format(
                    values=join_sep.join(value_transformer(value) for value in values)
                )
                if join_sep
                else " ".join(
                    [fmt.format(value=value_transformer(value)) for value in values]
                )
            )

        return wrapper


def field_(
    *,
    default: Any = None,
    metadata_cli: ReturnCliTypeFn | None = None,
    exclude: bool = False,
    **kwargs,
):
    """Custom dataclass field builder."""
    params_ = {
        "default": default,
        "metadata": {"cli": metadata_cli, "exclude": exclude},
        **kwargs,
    }

    if kwargs.get("default_factory", False):
        params_.pop("default", None)

    return dc_field(**params_)


@dataclass
class CustomBackendServer:
    """BackendServer base."""

    _app_uri: str = field_(default="", metadata_cli=None, exclude=True)

    @staticmethod
    def get_app_module(for_granian_target: bool = False, add_extra_api: bool = False):
        """Get the app module for the backend.

        Returns:
            The app module for the backend.
        """
        import reflex

        if for_granian_target:
            app_path = str(Path(reflex.__file__).parent / "app_module_for_backend.py")
        else:
            app_path = "reflex.app_module_for_backend"

        return f"{app_path}:{constants.CompileVars.APP}{f'.{constants.CompileVars.API}' if add_extra_api else ''}"

    def get_available_cpus(self) -> int:
        """Get available cpus."""
        return os.cpu_count() or 1

    def get_max_workers(self) -> int:
        """Get max workers."""
        # https://docs.gunicorn.org/en/latest/settings.html#workers
        return (os.cpu_count() or 1) * 4 + 1

    def get_recommended_workers(self) -> int:
        """Get recommended workers."""
        # https://docs.gunicorn.org/en/latest/settings.html#workers
        return (os.cpu_count() or 1) * 2 + 1

    def get_max_threads(self, wait_time_ms: int = 50, service_time_ms: int = 5) -> int:
        """Get max threads."""
        # https://engineering.zalando.com/posts/2019/04/how-to-set-an-ideal-thread-pool-size.html
        # Brian Goetz formula
        return int(self.get_available_cpus() * (1 + wait_time_ms / service_time_ms))

    def get_recommended_threads(
        self,
        target_reqs: int | None = None,
        wait_time_ms: int = 50,
        service_time_ms: int = 5,
    ) -> int:
        """Get recommended threads."""
        # https://engineering.zalando.com/posts/2019/04/how-to-set-an-ideal-thread-pool-size.html
        max_available_threads = self.get_max_threads()

        if target_reqs:
            # Little's law formula
            need_threads = target_reqs * (
                (wait_time_ms / 1000) + (service_time_ms / 1000)
            )
        else:
            need_threads = self.get_max_threads(wait_time_ms, service_time_ms)

        return int(
            max_available_threads
            if need_threads > max_available_threads
            else need_threads
        )

    def get_fields(self) -> dict[str, Field]:
        """Return all the fields."""
        return self.__dataclass_fields__

    def get_values(self) -> dict[str, Any]:
        """Return all values."""
        return {
            key: getattr(self, key)
            for key, field in self.__dataclass_fields__.items()
            if field.metadata["exclude"] is False
        }

    def is_default_value(self, key, value: Any | None = None) -> bool:
        """Check if the `value` is the same value from default context."""
        from dataclasses import MISSING

        field = self.get_fields()[key]
        if value is None:
            value = getattr(self, key, None)

        if field.default != MISSING:
            return value == field.default
        else:
            if field.default_factory != MISSING:
                return value == field.default_factory()

        return False

    @abstractmethod
    def check_import(self):
        """Check package importation."""
        raise NotImplementedError()

    @abstractmethod
    def setup(self, host: str, port: int, loglevel: LogLevel, env: Env):
        """Setup."""
        raise NotImplementedError()

    @abstractmethod
    def run_prod(self):
        """Run in production mode."""
        raise NotImplementedError()

    @abstractmethod
    def run_dev(self):
        """Run in development mode."""
        raise NotImplementedError()

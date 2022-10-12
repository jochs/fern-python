# This file was auto-generated by Fern from our API Definition.

# type: ignore
# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class TracedFile(pydantic.BaseModel):
    filename: str
    directory: str

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TracedFile.Validators.field("filename")
            def validate_filename(v: str, values: TracedFile.Partial) -> str:
                ...

            @TracedFile.Validators.field("directory")
            def validate_directory(v: str, values: TracedFile.Partial) -> str:
                ...
        """

        _filename_validators: typing.ClassVar[typing.List[TracedFile.Validators.FilenameValidator]] = []
        _directory_validators: typing.ClassVar[typing.List[TracedFile.Validators.DirectoryValidator]] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["filename"]
        ) -> typing.Callable[[TracedFile.Validators.FilenameValidator], TracedFile.Validators.FilenameValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["directory"]
        ) -> typing.Callable[[TracedFile.Validators.DirectoryValidator], TracedFile.Validators.DirectoryValidator]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "filename":
                    cls._filename_validators.append(validator)
                if field_name == "directory":
                    cls._directory_validators.append(validator)
                return validator

            return decorator

        class FilenameValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: TracedFile.Partial) -> str:
                ...

        class DirectoryValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: TracedFile.Partial) -> str:
                ...

    @pydantic.validator("filename")
    def _validate_filename(cls, v: str, values: str) -> str:
        for validator in TracedFile.Validators._filename_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("directory")
    def _validate_directory(cls, v: str, values: str) -> str:
        for validator in TracedFile.Validators._directory_validators:
            v = validator(v, values=values)
        return v

    class Partial(typing.TypedDict):
        filename: typing_extensions.NotRequired[str]
        directory: typing_extensions.NotRequired[str]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
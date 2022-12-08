# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class FileInfoV2(pydantic.BaseModel):
    filename: str
    directory: str
    contents: str
    editable: bool

    class Partial(typing_extensions.TypedDict):
        filename: typing_extensions.NotRequired[str]
        directory: typing_extensions.NotRequired[str]
        contents: typing_extensions.NotRequired[str]
        editable: typing_extensions.NotRequired[bool]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @FileInfoV2.Validators.root
            def validate(values: FileInfoV2.Partial) -> FileInfoV2.Partial:
                ...

            @FileInfoV2.Validators.field("filename")
            def validate_filename(filename: str, values: FileInfoV2.Partial) -> str:
                ...

            @FileInfoV2.Validators.field("directory")
            def validate_directory(directory: str, values: FileInfoV2.Partial) -> str:
                ...

            @FileInfoV2.Validators.field("contents")
            def validate_contents(contents: str, values: FileInfoV2.Partial) -> str:
                ...

            @FileInfoV2.Validators.field("editable")
            def validate_editable(editable: bool, values: FileInfoV2.Partial) -> bool:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[FileInfoV2.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[FileInfoV2.Validators._RootValidator]] = []
        _filename_pre_validators: typing.ClassVar[typing.List[FileInfoV2.Validators.FilenameValidator]] = []
        _filename_post_validators: typing.ClassVar[typing.List[FileInfoV2.Validators.FilenameValidator]] = []
        _directory_pre_validators: typing.ClassVar[typing.List[FileInfoV2.Validators.DirectoryValidator]] = []
        _directory_post_validators: typing.ClassVar[typing.List[FileInfoV2.Validators.DirectoryValidator]] = []
        _contents_pre_validators: typing.ClassVar[typing.List[FileInfoV2.Validators.ContentsValidator]] = []
        _contents_post_validators: typing.ClassVar[typing.List[FileInfoV2.Validators.ContentsValidator]] = []
        _editable_pre_validators: typing.ClassVar[typing.List[FileInfoV2.Validators.EditableValidator]] = []
        _editable_post_validators: typing.ClassVar[typing.List[FileInfoV2.Validators.EditableValidator]] = []

        @classmethod
        def root(cls, *, pre: bool = False) -> FileInfoV2.Validators._RootValidator:
            def decorator(validator: typing.Any) -> typing.Any:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["filename"], *, pre: bool = False
        ) -> typing.Callable[[FileInfoV2.Validators.FilenameValidator], FileInfoV2.Validators.FilenameValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["directory"], *, pre: bool = False
        ) -> typing.Callable[[FileInfoV2.Validators.DirectoryValidator], FileInfoV2.Validators.DirectoryValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["contents"], *, pre: bool = False
        ) -> typing.Callable[[FileInfoV2.Validators.ContentsValidator], FileInfoV2.Validators.ContentsValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["editable"], *, pre: bool = False
        ) -> typing.Callable[[FileInfoV2.Validators.EditableValidator], FileInfoV2.Validators.EditableValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "filename":
                    if pre:
                        cls._filename_pre_validators.append(validator)
                    else:
                        cls._filename_post_validators.append(validator)
                if field_name == "directory":
                    if pre:
                        cls._directory_pre_validators.append(validator)
                    else:
                        cls._directory_post_validators.append(validator)
                if field_name == "contents":
                    if pre:
                        cls._contents_pre_validators.append(validator)
                    else:
                        cls._contents_post_validators.append(validator)
                if field_name == "editable":
                    if pre:
                        cls._editable_pre_validators.append(validator)
                    else:
                        cls._editable_post_validators.append(validator)
                return validator

            return decorator

        class FilenameValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: FileInfoV2.Partial) -> str:
                ...

        class DirectoryValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: FileInfoV2.Partial) -> str:
                ...

        class ContentsValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: FileInfoV2.Partial) -> str:
                ...

        class EditableValidator(typing_extensions.Protocol):
            def __call__(self, __v: bool, __values: FileInfoV2.Partial) -> bool:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: FileInfoV2.Partial) -> FileInfoV2.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: FileInfoV2.Partial) -> FileInfoV2.Partial:
        for validator in FileInfoV2.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: FileInfoV2.Partial) -> FileInfoV2.Partial:
        for validator in FileInfoV2.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("filename", pre=True)
    def _pre_validate_filename(cls, v: str, values: FileInfoV2.Partial) -> str:
        for validator in FileInfoV2.Validators._filename_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("filename", pre=False)
    def _post_validate_filename(cls, v: str, values: FileInfoV2.Partial) -> str:
        for validator in FileInfoV2.Validators._filename_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("directory", pre=True)
    def _pre_validate_directory(cls, v: str, values: FileInfoV2.Partial) -> str:
        for validator in FileInfoV2.Validators._directory_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("directory", pre=False)
    def _post_validate_directory(cls, v: str, values: FileInfoV2.Partial) -> str:
        for validator in FileInfoV2.Validators._directory_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("contents", pre=True)
    def _pre_validate_contents(cls, v: str, values: FileInfoV2.Partial) -> str:
        for validator in FileInfoV2.Validators._contents_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("contents", pre=False)
    def _post_validate_contents(cls, v: str, values: FileInfoV2.Partial) -> str:
        for validator in FileInfoV2.Validators._contents_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("editable", pre=True)
    def _pre_validate_editable(cls, v: bool, values: FileInfoV2.Partial) -> bool:
        for validator in FileInfoV2.Validators._editable_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("editable", pre=False)
    def _post_validate_editable(cls, v: bool, values: FileInfoV2.Partial) -> bool:
        for validator in FileInfoV2.Validators._editable_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        extra = pydantic.Extra.forbid

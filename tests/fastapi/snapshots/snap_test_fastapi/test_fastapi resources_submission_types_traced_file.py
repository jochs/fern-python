import typing

import pydantic
import typing_extensions


class TracedFile(pydantic.BaseModel):
    filename: str
    directory: str

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    @pydantic.validator("filename")
    def _validate_filename(cls, filename: str) -> str:
        for validator in TracedFile.Validators._filename_validators:
            filename = validator(filename)
        return filename

    @pydantic.validator("directory")
    def _validate_directory(cls, directory: str) -> str:
        for validator in TracedFile.Validators._directory_validators:
            directory = validator(directory)
        return directory

    class Validators:
        _filename_validators: typing.ClassVar[typing.List[typing.Callable[[str], str]]] = []
        _directory_validators: typing.ClassVar[typing.List[typing.Callable[[str], str]]] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["filename"]
        ) -> typing.Callable[[typing.Callable[[str], str]], typing.Callable[[str], str]]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["directory"]
        ) -> typing.Callable[[typing.Callable[[str], str]], typing.Callable[[str], str]]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "filename":
                    cls._filename_validators.append(validator)
                elif field_name == "directory":
                    cls._directory_validators.append(validator)
                else:
                    raise RuntimeError("Field does not exist on TracedFile: " + field_name)

                return validator

            return decorator

    class Config:
        frozen = True

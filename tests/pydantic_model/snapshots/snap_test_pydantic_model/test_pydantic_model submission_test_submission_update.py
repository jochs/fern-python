import typing

import pydantic
import typing_extensions

from .test_submission_update_info import TestSubmissionUpdateInfo


class TestSubmissionUpdate(pydantic.BaseModel):
    update_time: str = pydantic.Field(alias="updateTime")
    update_info: TestSubmissionUpdateInfo = pydantic.Field(alias="updateInfo")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    @pydantic.validator("update_time")
    def _validate_update_time(cls, update_time: str) -> str:
        for validator in TestSubmissionUpdate.Validators._update_time_validators:
            update_time = validator(update_time)
        return update_time

    @pydantic.validator("update_info")
    def _validate_update_info(cls, update_info: TestSubmissionUpdateInfo) -> TestSubmissionUpdateInfo:
        for validator in TestSubmissionUpdate.Validators._update_info_validators:
            update_info = validator(update_info)
        return update_info

    class Validators:
        _update_time_validators: typing.ClassVar[typing.List[typing.Callable[[str], str]]] = []
        _update_info_validators: typing.ClassVar[
            typing.List[typing.Callable[[TestSubmissionUpdateInfo], TestSubmissionUpdateInfo]]
        ] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["update_time"]
        ) -> typing.Callable[[typing.Callable[[str], str]], typing.Callable[[str], str]]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["update_info"]
        ) -> typing.Callable[
            [typing.Callable[[TestSubmissionUpdateInfo], TestSubmissionUpdateInfo]],
            typing.Callable[[TestSubmissionUpdateInfo], TestSubmissionUpdateInfo],
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "update_time":
                    cls._update_time_validators.append(validator)
                elif field_name == "update_info":
                    cls._update_info_validators.append(validator)
                else:
                    raise RuntimeError("Field does not exist on TestSubmissionUpdate: " + field_name)

                return validator

            return decorator

    class Config:
        frozen = True
        allow_population_by_field_name = True

import typing

import pydantic
import typing_extensions

from .submission_id import SubmissionId


class StopRequest(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")

    @pydantic.validator("submission_id")
    def _validate_submission_id(cls, submission_id: SubmissionId) -> SubmissionId:
        for validator in StopRequest.Validators._submission_id:
            submission_id = validator(submission_id)
        return submission_id

    class Validators:
        _submission_id: typing.ClassVar[SubmissionId] = []

        @typing.overload
        @classmethod
        def field(submission_id: typing_extensions.Literal["submission_id"]) -> SubmissionId:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "submission_id":
                    cls._submission_id.append(validator)  # type: ignore
                else:
                    raise RuntimeError("Field does not exist on StopRequest: " + field_name)

                return validator

            return validator  # type: ignore

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True

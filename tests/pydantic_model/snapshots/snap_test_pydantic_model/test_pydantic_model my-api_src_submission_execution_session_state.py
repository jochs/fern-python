import typing

import pydantic

from ..commons.language import Language
from .execution_session_status import ExecutionSessionStatus


class ExecutionSessionState(pydantic.BaseModel):
    last_time_contacted: typing.Optional[str] = pydantic.Field(alias="lastTimeContacted")
    session_id: str = pydantic.Field(alias="sessionId")
    is_warm_instance: bool = pydantic.Field(alias="isWarmInstance")
    aws_task_id: typing.Optional[str] = pydantic.Field(alias="awsTaskId")
    language: Language
    status: ExecutionSessionStatus

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    class Config:
        allow_population_by_field_name = True
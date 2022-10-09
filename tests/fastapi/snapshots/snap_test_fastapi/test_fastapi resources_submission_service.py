import abc
import inspect
import typing

import fastapi

from ..commons.types.language import Language
from .types.execution_session_response import ExecutionSessionResponse
from .types.get_execution_session_state_response import GetExecutionSessionStateResponse


class AbstractExecutionSesssionManagementService(abc.ABC):
    """
    AbstractExecutionSesssionManagementService is an abstract class containing the methods that your
    ExecutionSesssionManagementService implementation should implement.

    Each method is associated with an API route, which will be registered
    with FastAPI when you register your implementation using Fern's register()
    function.
    """

    @abc.abstractmethod
    def createExecutionSession(self, language: Language) -> ExecutionSessionResponse:
        ...

    @abc.abstractmethod
    def getExecutionSession(self, session_id: str) -> typing.Optional[ExecutionSessionResponse]:
        ...

    @abc.abstractmethod
    def stopExecutionSession(self, session_id: str) -> None:
        ...

    @abc.abstractmethod
    def getExecutionSessionsState(self) -> GetExecutionSessionStateResponse:
        ...

    """
	Below are internal methods used by Fern to register your implementation.
	You can ignore them.
	"""

    @classmethod
    def _init_fern(cls, router: fastapi.APIRouter) -> None:
        cls.__init_createExecutionSession(router=router)
        cls.__init_getExecutionSession(router=router)
        cls.__init_stopExecutionSession(router=router)
        cls.__init_getExecutionSessionsState(router=router)

    @classmethod
    def __init_createExecutionSession(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature()
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if parameter_name == "language":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        cls.createExecutionSession.__signature__ = endpoint_function.replace(parameters=new_parameters)
        cls.createExecutionSession = router.post(  # type: ignore
            path="/create-session/{language}", response_model=ExecutionSessionResponse
        )(cls.createExecutionSession)

    @classmethod
    def __init_getExecutionSession(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature()
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if parameter_name == "session_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        cls.getExecutionSession.__signature__ = endpoint_function.replace(parameters=new_parameters)
        cls.getExecutionSession = router.get(  # type: ignore
            path="/{session_id}", response_model=typing.Optional[ExecutionSessionResponse]
        )(cls.getExecutionSession)

    @classmethod
    def __init_stopExecutionSession(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature()
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if parameter_name == "session_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        cls.stopExecutionSession.__signature__ = endpoint_function.replace(parameters=new_parameters)
        cls.stopExecutionSession = router.delete(path="/stop/{session_id}")(cls.stopExecutionSession)  # type: ignore

    @classmethod
    def __init_getExecutionSessionsState(cls, router: fastapi.APIRouter) -> None:
        cls.getExecutionSessionsState = router.get(  # type: ignore
            path="/execution-sessions-state", response_model=GetExecutionSessionStateResponse
        )(cls.getExecutionSessionsState)

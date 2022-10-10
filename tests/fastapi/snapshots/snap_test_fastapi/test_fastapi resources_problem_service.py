import abc
import inspect
import typing

import fastapi

from ..commons.types.problem_id import ProblemId
from .types.create_problem_request import CreateProblemRequest
from .types.create_problem_response import CreateProblemResponse
from .types.get_default_starter_files_request import GetDefaultStarterFilesRequest
from .types.get_default_starter_files_response import GetDefaultStarterFilesResponse
from .types.update_problem_response import UpdateProblemResponse


class AbstractProblemCrudService(abc.ABC):
    """
    AbstractProblemCrudService is an abstract class containing the methods that your
    ProblemCrudService implementation should implement.

    Each method is associated with an API route, which will be registered
    with FastAPI when you register your implementation using Fern's register()
    function.
    """

    @abc.abstractmethod
    def createProblem(self, *, request: CreateProblemRequest) -> CreateProblemResponse:
        ...

    @abc.abstractmethod
    def updateProblem(self, *, request: CreateProblemRequest, problem_id: ProblemId) -> UpdateProblemResponse:
        ...

    @abc.abstractmethod
    def deleteProblem(self, *, problem_id: ProblemId) -> None:
        ...

    @abc.abstractmethod
    def getDefaultStarterFiles(self, *, request: GetDefaultStarterFilesRequest) -> GetDefaultStarterFilesResponse:
        ...

    """
    Below are internal methods used by Fern to register your implementation.
    You can ignore them.
    """

    @classmethod
    def _init_fern(cls, router: fastapi.APIRouter) -> None:
        cls.__init_createProblem(router=router)
        cls.__init_updateProblem(router=router)
        cls.__init_deleteProblem(router=router)
        cls.__init_getDefaultStarterFiles(router=router)

    @classmethod
    def __init_createProblem(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature()
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if parameter_name == "request":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            else:
                new_parameters.append(parameter)
        cls.createProblem.__signature__ = endpoint_function.replace(parameters=new_parameters)
        cls.createProblem = router.post(path="/create", response_model=CreateProblemResponse)(  # type: ignore
            cls.createProblem
        )

    @classmethod
    def __init_updateProblem(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature()
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if parameter_name == "request":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "problem_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        cls.updateProblem.__signature__ = endpoint_function.replace(parameters=new_parameters)
        cls.updateProblem = router.post(  # type: ignore
            path="/update/{problem_id}", response_model=UpdateProblemResponse
        )(cls.updateProblem)

    @classmethod
    def __init_deleteProblem(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature()
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if parameter_name == "problem_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        cls.deleteProblem.__signature__ = endpoint_function.replace(parameters=new_parameters)
        cls.deleteProblem = router.delete(path="/delete/{problem_id}")(cls.deleteProblem)  # type: ignore

    @classmethod
    def __init_getDefaultStarterFiles(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature()
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if parameter_name == "request":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            else:
                new_parameters.append(parameter)
        cls.getDefaultStarterFiles.__signature__ = endpoint_function.replace(parameters=new_parameters)
        cls.getDefaultStarterFiles = router.post(  # type: ignore
            path="/default-starter-files", response_model=GetDefaultStarterFilesResponse
        )(cls.getDefaultStarterFiles)

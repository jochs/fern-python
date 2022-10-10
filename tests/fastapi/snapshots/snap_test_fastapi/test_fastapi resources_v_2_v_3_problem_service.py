import abc
import inspect
import typing

import fastapi

from ....commons.types.problem_id import ProblemId
from .types.lightweight_problem_info_v_2 import LightweightProblemInfoV2
from .types.problem_info_v_2 import ProblemInfoV2


class AbstractProblemInfoServicV2(abc.ABC):
    """
    AbstractProblemInfoServicV2 is an abstract class containing the methods that your
    ProblemInfoServicV2 implementation should implement.

    Each method is associated with an API route, which will be registered
    with FastAPI when you register your implementation using Fern's register()
    function.
    """

    @abc.abstractmethod
    def getLightweightProblems(self) -> typing.List[LightweightProblemInfoV2]:
        ...

    @abc.abstractmethod
    def getProblems(self) -> typing.List[ProblemInfoV2]:
        ...

    @abc.abstractmethod
    def getLatestProblem(self, *, problem_id: ProblemId) -> ProblemInfoV2:
        ...

    @abc.abstractmethod
    def getProblemVersion(self, *, problem_id: ProblemId, problem_version: int) -> ProblemInfoV2:
        ...

    """
    Below are internal methods used by Fern to register your implementation.
    You can ignore them.
    """

    @classmethod
    def _init_fern(cls, router: fastapi.APIRouter) -> None:
        cls.__init_getLightweightProblems(router=router)
        cls.__init_getProblems(router=router)
        cls.__init_getLatestProblem(router=router)
        cls.__init_getProblemVersion(router=router)

    @classmethod
    def __init_getLightweightProblems(cls, router: fastapi.APIRouter) -> None:
        cls.getLightweightProblems = router.get(  # type: ignore
            path="/lightweight-problem-info", response_model=typing.List[LightweightProblemInfoV2]
        )(cls.getLightweightProblems)

    @classmethod
    def __init_getProblems(cls, router: fastapi.APIRouter) -> None:
        cls.getProblems = router.get(path="/problem-info", response_model=typing.List[ProblemInfoV2])(  # type: ignore
            cls.getProblems
        )

    @classmethod
    def __init_getLatestProblem(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature()
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if parameter_name == "problem_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        cls.getLatestProblem.__signature__ = endpoint_function.replace(parameters=new_parameters)
        cls.getLatestProblem = router.get(  # type: ignore
            path="/problem-info/{problem_id}", response_model=ProblemInfoV2
        )(cls.getLatestProblem)

    @classmethod
    def __init_getProblemVersion(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature()
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if parameter_name == "problem_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "problem_version":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        cls.getProblemVersion.__signature__ = endpoint_function.replace(parameters=new_parameters)
        cls.getProblemVersion = router.get(  # type: ignore
            path="/problem-info/{problem_id}/version/{problem_version}", response_model=ProblemInfoV2
        )(cls.getProblemVersion)

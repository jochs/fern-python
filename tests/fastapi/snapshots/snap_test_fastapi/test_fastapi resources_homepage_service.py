import abc
import inspect
import typing

import fastapi

from ..commons.types.problem_id import ProblemId


class AbstractHomepageProblemService(abc.ABC):
    """
    AbstractHomepageProblemService is an abstract class containing the methods that your
    HomepageProblemService implementation should implement.

    Each method is associated with an API route, which will be registered
    with FastAPI when you register your implementation using Fern's register()
    function.
    """

    @abc.abstractmethod
    def getHomepageProblems(self) -> typing.List[ProblemId]:
        ...

    @abc.abstractmethod
    def setHomepageProblems(self, request: typing.List[ProblemId]) -> None:
        ...

    """
    Below are internal methods used by Fern to register your implementation.
    You can ignore them.
    """

    @classmethod
    def _init_fern(cls, router: fastapi.APIRouter) -> None:
        cls.__init_getHomepageProblems(router=router)
        cls.__init_setHomepageProblems(router=router)

    @classmethod
    def __init_getHomepageProblems(cls, router: fastapi.APIRouter) -> None:
        cls.getHomepageProblems = router.get(path="/", response_model=typing.List[ProblemId])(  # type: ignore
            cls.getHomepageProblems
        )

    @classmethod
    def __init_setHomepageProblems(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature()
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if parameter_name == "request":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            else:
                new_parameters.append(parameter)
        cls.setHomepageProblems.__signature__ = endpoint_function.replace(parameters=new_parameters)
        cls.setHomepageProblems = router.post(path="/")(cls.setHomepageProblems)  # type: ignore

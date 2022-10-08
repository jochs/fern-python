import abc
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
        cls.setHomepageProblems = router.post(path="/")(cls.setHomepageProblems)  # type: ignore

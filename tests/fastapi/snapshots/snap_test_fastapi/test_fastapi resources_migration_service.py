import abc
import typing

import fastapi

from .types.migration import Migration


class AbstractMigrationInfoService(abc.ABC):
    """
    AbstractMigrationInfoService is an abstract class containing the methods that your
    MigrationInfoService implementation should implement.

    Each method is associated with an API route, which will be registered
    with FastAPI when you register your implementation using Fern's register()
    function.
    """

    @abc.abstractmethod
    def getAttemptedMigrations(self) -> typing.List[Migration]:
        ...

    """
	Below are internal methods used by Fern to register your implementation.
	You can ignore them.
	"""

    @classmethod
    def _init_fern(cls, router: fastapi.APIRouter) -> None:
        cls.__init_getAttemptedMigrations(router=router)

    @classmethod
    def __init_getAttemptedMigrations(cls, router: fastapi.APIRouter) -> None:
        cls.getAttemptedMigrations = router.get(path="/all", response_model=typing.List[Migration])(  # type: ignore
            cls.getAttemptedMigrations
        )

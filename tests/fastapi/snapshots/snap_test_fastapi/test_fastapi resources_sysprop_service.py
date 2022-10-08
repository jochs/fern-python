import abc
import typing

import fastapi

from ..commons.types.language import Language


class AbstractSysPropCrudService(abc.ABC):
    """
    AbstractSysPropCrudService is an abstract class containing the methods that your
    SysPropCrudService implementation should implement.

    Each method is associated with an API route, which will be registered
    with FastAPI when you register your implementation using Fern's register()
    function.
    """

    @abc.abstractmethod
    def setNumWarmInstances(self, language: Language, num_warm_instances: int) -> None:
        ...

    @abc.abstractmethod
    def getNumWarmInstances(self) -> typing.Dict[Language, int]:
        ...

    """
	Below are internal methods used by Fern to register your implementation.
	You can ignore them.
	"""

    @classmethod
    def _init_fern(cls, router: fastapi.APIRouter) -> None:
        cls.__init_setNumWarmInstances(router=router)
        cls.__init_getNumWarmInstances(router=router)

    @classmethod
    def __init_setNumWarmInstances(cls, router: fastapi.APIRouter) -> None:
        cls.setNumWarmInstances = router.put(  # type: ignore
            path="/num-warm-instances/{language}/{num_warm_instances}"
        )(cls.setNumWarmInstances)

    @classmethod
    def __init_getNumWarmInstances(cls, router: fastapi.APIRouter) -> None:
        cls.getNumWarmInstances = router.get(  # type: ignore
            path="/num-warm-instances", response_model=typing.Dict[Language, int]
        )(cls.getNumWarmInstances)

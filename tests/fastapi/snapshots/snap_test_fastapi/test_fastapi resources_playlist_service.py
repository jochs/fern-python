import abc
import inspect
import typing

import fastapi

from .types.playlist import Playlist
from .types.playlist_create_request import PlaylistCreateRequest
from .types.playlist_id import PlaylistId
from .types.update_playlist_request import UpdatePlaylistRequest


class AbstractPlaylistCrudService(abc.ABC):
    """
    AbstractPlaylistCrudService is an abstract class containing the methods that your
    PlaylistCrudService implementation should implement.

    Each method is associated with an API route, which will be registered
    with FastAPI when you register your implementation using Fern's register()
    function.
    """

    @abc.abstractmethod
    def createPlaylist(self, request: PlaylistCreateRequest) -> Playlist:
        ...

    @abc.abstractmethod
    def getPlaylists(self, limit: typing.Optional[int], other_field: str) -> typing.List[Playlist]:
        ...

    @abc.abstractmethod
    def getPlaylist(self, playlist_id: PlaylistId) -> Playlist:
        ...

    @abc.abstractmethod
    def updatePlaylist(
        self, request: typing.Optional[UpdatePlaylistRequest], playlist_id: PlaylistId
    ) -> typing.Optional[Playlist]:
        ...

    @abc.abstractmethod
    def deletePlaylist(self, playlist_id: PlaylistId) -> None:
        ...

    """
	Below are internal methods used by Fern to register your implementation.
	You can ignore them.
	"""

    @classmethod
    def _init_fern(cls, router: fastapi.APIRouter) -> None:
        cls.__init_createPlaylist(router=router)
        cls.__init_getPlaylists(router=router)
        cls.__init_getPlaylist(router=router)
        cls.__init_updatePlaylist(router=router)
        cls.__init_deletePlaylist(router=router)

    @classmethod
    def __init_createPlaylist(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature()
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if parameter_name == "request":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            else:
                new_parameters.append(parameter)
        cls.createPlaylist.__signature__ = endpoint_function.replace(parameters=new_parameters)
        cls.createPlaylist = router.post(path="/create", response_model=Playlist)(cls.createPlaylist)  # type: ignore

    @classmethod
    def __init_getPlaylists(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature()
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if parameter_name == "limit":
                new_parameters.append(parameter.replace(default=fastapi.Query(default=None)))
            elif parameter_name == "other_field":
                new_parameters.append(parameter.replace(default=fastapi.Query(alias="otherField")))
            else:
                new_parameters.append(parameter)
        cls.getPlaylists.__signature__ = endpoint_function.replace(parameters=new_parameters)
        cls.getPlaylists = router.get(path="/all", response_model=typing.List[Playlist])(  # type: ignore
            cls.getPlaylists
        )

    @classmethod
    def __init_getPlaylist(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature()
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if parameter_name == "playlist_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        cls.getPlaylist.__signature__ = endpoint_function.replace(parameters=new_parameters)
        cls.getPlaylist = router.get(path="/{playlist_id}", response_model=Playlist)(cls.getPlaylist)  # type: ignore

    @classmethod
    def __init_updatePlaylist(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature()
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if parameter_name == "request":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "playlist_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        cls.updatePlaylist.__signature__ = endpoint_function.replace(parameters=new_parameters)
        cls.updatePlaylist = router.put(  # type: ignore
            path="/{playlist_id}", response_model=typing.Optional[Playlist]
        )(cls.updatePlaylist)

    @classmethod
    def __init_deletePlaylist(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature()
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if parameter_name == "playlist_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        cls.deletePlaylist.__signature__ = endpoint_function.replace(parameters=new_parameters)
        cls.deletePlaylist = router.delete(path="/{playlist_id}")(cls.deletePlaylist)  # type: ignore

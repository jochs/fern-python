import abc
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
    def getPlaylists(self, limit: typing.Optional[int]) -> typing.List[Playlist]:
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
        cls.createPlaylist = router.post(path="/create", response_model=Playlist)(cls.createPlaylist)  # type: ignore

    @classmethod
    def __init_getPlaylists(cls, router: fastapi.APIRouter) -> None:
        cls.getPlaylists = router.get(path="/all", response_model=typing.List[Playlist])(  # type: ignore
            cls.getPlaylists
        )

    @classmethod
    def __init_getPlaylist(cls, router: fastapi.APIRouter) -> None:
        cls.getPlaylist = router.get(path="/{playlist_id}", response_model=Playlist)(cls.getPlaylist)  # type: ignore

    @classmethod
    def __init_updatePlaylist(cls, router: fastapi.APIRouter) -> None:
        cls.updatePlaylist = router.put(  # type: ignore
            path="/{playlist_id}", response_model=typing.Optional[Playlist]
        )(cls.updatePlaylist)

    @classmethod
    def __init_deletePlaylist(cls, router: fastapi.APIRouter) -> None:
        cls.deletePlaylist = router.delete(path="/{playlist_id}")(cls.deletePlaylist)  # type: ignore

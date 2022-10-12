# This file was auto-generated by Fern from our API Definition.

# type: ignore
# flake8: noqa
# fmt: off
# isort: skip_file

import abc
import inspect
import typing

import fastapi

from ...core.abstract_fern_service import AbstractFernService
from ...core.route_args import get_route_args
from ...security import ApiAuth, FernAuth
from .types.playlist import Playlist
from .types.playlist_create_request import PlaylistCreateRequest
from .types.update_playlist_request import UpdatePlaylistRequest


class AbstractPlaylistCrudService(AbstractFernService):
    """
    AbstractPlaylistCrudService is an abstract class containing the methods that your
    PlaylistCrudService implementation should implement.

    Each method is associated with an API route, which will be registered
    with FastAPI when you register your implementation using Fern's register()
    function.
    """

    @abc.abstractmethod
    def create_playlist(self, *, body: PlaylistCreateRequest, service_param: int, auth: ApiAuth) -> Playlist:
        ...

    @abc.abstractmethod
    def get_playlists(
        self, *, service_param: int, limit: typing.Optional[int], other_field: str, auth: ApiAuth
    ) -> typing.List[Playlist]:
        ...

    @abc.abstractmethod
    def get_playlist(self, *, service_param: int, playlist_id: str) -> Playlist:
        ...

    @abc.abstractmethod
    def update_playlist(
        self, *, body: typing.Optional[UpdatePlaylistRequest], service_param: int, playlist_id: str, auth: ApiAuth
    ) -> typing.Optional[Playlist]:
        ...

    @abc.abstractmethod
    def delete_playlist(self, *, service_param: int, playlist_id: str, auth: ApiAuth) -> None:
        ...

    """
    Below are internal methods used by Fern to register your implementation.
    You can ignore them.
    """

    @classmethod
    def _init_fern(cls, router: fastapi.APIRouter) -> None:
        cls.__init_create_playlist(router=router)
        cls.__init_get_playlists(router=router)
        cls.__init_get_playlist(router=router)
        cls.__init_update_playlist(router=router)
        cls.__init_delete_playlist(router=router)

    @classmethod
    def __init_create_playlist(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.create_playlist)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "service_param":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "auth":
                new_parameters.append(parameter.replace(default=fastapi.Depends(FernAuth)))
            else:
                new_parameters.append(parameter)
        setattr(cls.create_playlist, "__signature__", endpoint_function.replace(parameters=new_parameters))

        cls.create_playlist = router.post(  # type: ignore
            path="/v2/playlist/{service_param}/create", response_model=Playlist, **get_route_args(cls.create_playlist)
        )(cls.create_playlist)

    @classmethod
    def __init_get_playlists(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.get_playlists)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "service_param":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "limit":
                new_parameters.append(parameter.replace(default=fastapi.Query(default=None)))
            elif parameter_name == "other_field":
                new_parameters.append(parameter.replace(default=fastapi.Query(alias="otherField")))
            elif parameter_name == "auth":
                new_parameters.append(parameter.replace(default=fastapi.Depends(FernAuth)))
            else:
                new_parameters.append(parameter)
        setattr(cls.get_playlists, "__signature__", endpoint_function.replace(parameters=new_parameters))

        cls.get_playlists = router.get(  # type: ignore
            path="/v2/playlist/{service_param}/all",
            response_model=typing.List[Playlist],
            **get_route_args(cls.get_playlists),
        )(cls.get_playlists)

    @classmethod
    def __init_get_playlist(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.get_playlist)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "service_param":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "playlist_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls.get_playlist, "__signature__", endpoint_function.replace(parameters=new_parameters))

        cls.get_playlist = router.get(  # type: ignore
            path="/v2/playlist/{service_param}/{playlist_id}",
            response_model=Playlist,
            **get_route_args(cls.get_playlist),
        )(cls.get_playlist)

    @classmethod
    def __init_update_playlist(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.update_playlist)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "service_param":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "playlist_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "auth":
                new_parameters.append(parameter.replace(default=fastapi.Depends(FernAuth)))
            else:
                new_parameters.append(parameter)
        setattr(cls.update_playlist, "__signature__", endpoint_function.replace(parameters=new_parameters))

        cls.update_playlist = router.put(  # type: ignore
            path="/v2/playlist/{service_param}/{playlist_id}",
            response_model=typing.Optional[Playlist],
            **get_route_args(cls.update_playlist),
        )(cls.update_playlist)

    @classmethod
    def __init_delete_playlist(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.delete_playlist)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "service_param":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "playlist_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "auth":
                new_parameters.append(parameter.replace(default=fastapi.Depends(FernAuth)))
            else:
                new_parameters.append(parameter)
        setattr(cls.delete_playlist, "__signature__", endpoint_function.replace(parameters=new_parameters))

        cls.delete_playlist = router.delete(  # type: ignore
            path="/v2/playlist/{service_param}/{playlist_id}", **get_route_args(cls.delete_playlist)
        )(cls.delete_playlist)
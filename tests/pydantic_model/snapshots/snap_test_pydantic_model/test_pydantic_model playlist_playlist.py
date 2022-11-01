# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ..commons.user_id import UserId
from .playlist_create_request import PlaylistCreateRequest
from .playlist_id import PlaylistId


class Playlist(PlaylistCreateRequest):
    playlist_id: PlaylistId
    owner_id: UserId = pydantic.Field(alias="owner-id")

    class Partial(PlaylistCreateRequest.Partial):
        playlist_id: typing_extensions.NotRequired[PlaylistId]
        owner_id: typing_extensions.NotRequired[UserId]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @Playlist.Validators.root
            def validate(values: Playlist.Partial) -> Playlist.Partial:
                ...

            @Playlist.Validators.field("playlist_id")
            def validate_playlist_id(playlist_id: PlaylistId, values: Playlist.Partial) -> PlaylistId:
                ...

            @Playlist.Validators.field("owner_id")
            def validate_owner_id(owner_id: UserId, values: Playlist.Partial) -> UserId:
                ...
        """

        _validators: typing.ClassVar[typing.List[typing.Callable[[Playlist.Partial], Playlist.Partial]]] = []
        _playlist_id_validators: typing.ClassVar[typing.List[Playlist.Validators.PlaylistIdValidator]] = []
        _owner_id_validators: typing.ClassVar[typing.List[Playlist.Validators.OwnerIdValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[Playlist.Partial], Playlist.Partial]
        ) -> typing.Callable[[Playlist.Partial], Playlist.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["playlist_id"]
        ) -> typing.Callable[[Playlist.Validators.PlaylistIdValidator], Playlist.Validators.PlaylistIdValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["owner_id"]
        ) -> typing.Callable[[Playlist.Validators.OwnerIdValidator], Playlist.Validators.OwnerIdValidator]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "playlist_id":
                    cls._playlist_id_validators.append(validator)
                if field_name == "owner_id":
                    cls._owner_id_validators.append(validator)
                return validator

            return decorator

        class PlaylistIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: PlaylistId, __values: Playlist.Partial) -> PlaylistId:
                ...

        class OwnerIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: UserId, __values: Playlist.Partial) -> UserId:
                ...

    @pydantic.root_validator
    def _validate(cls, values: Playlist.Partial) -> Playlist.Partial:
        for validator in Playlist.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("playlist_id")
    def _validate_playlist_id(cls, v: PlaylistId, values: Playlist.Partial) -> PlaylistId:
        for validator in Playlist.Validators._playlist_id_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("owner_id")
    def _validate_owner_id(cls, v: UserId, values: Playlist.Partial) -> UserId:
        for validator in Playlist.Validators._owner_id_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True

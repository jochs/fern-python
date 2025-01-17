# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .resources.imdb.client import AsyncImdbClient, ImdbClient


class SeedApi:
    def __init__(
        self,
        *,
        base_url: str,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        timeout: typing.Optional[float] = 60
    ):
        self._client_wrapper = SyncClientWrapper(
            base_url=base_url, token=token, httpx_client=httpx.Client(timeout=timeout)
        )
        self.imdb = ImdbClient(client_wrapper=self._client_wrapper)


class AsyncSeedApi:
    def __init__(
        self,
        *,
        base_url: str,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        timeout: typing.Optional[float] = 60
    ):
        self._client_wrapper = AsyncClientWrapper(
            base_url=base_url, token=token, httpx_client=httpx.AsyncClient(timeout=timeout)
        )
        self.imdb = AsyncImdbClient(client_wrapper=self._client_wrapper)

# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .resources.property_based_error.client import AsyncPropertyBasedErrorClient, PropertyBasedErrorClient


class SeedApi:
    def __init__(self, *, base_url: str, timeout: typing.Optional[float] = 60):
        self._client_wrapper = SyncClientWrapper(base_url=base_url, httpx_client=httpx.Client(timeout=timeout))
        self.property_based_error = PropertyBasedErrorClient(client_wrapper=self._client_wrapper)


class AsyncSeedApi:
    def __init__(self, *, base_url: str, timeout: typing.Optional[float] = 60):
        self._client_wrapper = AsyncClientWrapper(base_url=base_url, httpx_client=httpx.AsyncClient(timeout=timeout))
        self.property_based_error = AsyncPropertyBasedErrorClient(client_wrapper=self._client_wrapper)
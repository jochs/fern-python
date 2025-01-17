# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import SeedMultiUrlEnvironmentEnvironment
from .resources.ec_2.client import AsyncEc2Client, Ec2Client
from .resources.s_3.client import AsyncS3Client, S3Client


class SeedMultiUrlEnvironment:
    def __init__(
        self,
        *,
        environment: SeedMultiUrlEnvironmentEnvironment = SeedMultiUrlEnvironmentEnvironment.PRODUCTION,
        token: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = 60
    ):
        self._client_wrapper = SyncClientWrapper(
            environment=environment, token=token, httpx_client=httpx.Client(timeout=timeout)
        )
        self.ec_2 = Ec2Client(client_wrapper=self._client_wrapper)
        self.s_3 = S3Client(client_wrapper=self._client_wrapper)


class AsyncSeedMultiUrlEnvironment:
    def __init__(
        self,
        *,
        environment: SeedMultiUrlEnvironmentEnvironment = SeedMultiUrlEnvironmentEnvironment.PRODUCTION,
        token: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = 60
    ):
        self._client_wrapper = AsyncClientWrapper(
            environment=environment, token=token, httpx_client=httpx.AsyncClient(timeout=timeout)
        )
        self.ec_2 = AsyncEc2Client(client_wrapper=self._client_wrapper)
        self.s_3 = AsyncS3Client(client_wrapper=self._client_wrapper)

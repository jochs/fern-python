# This file was auto-generated by Fern from our API Definition.

import typing

from backports.cached_property import cached_property

from .environment import FernIrEnvironment
from .resources.admin.client import AdminClient, AsyncAdminClient
from .resources.homepage.client import AsyncHomepageClient, HomepageClient
from .resources.migration.client import AsyncMigrationClient, MigrationClient
from .resources.playlist.client import AsyncPlaylistClient, PlaylistClient
from .resources.problem.client import AsyncProblemClient, ProblemClient
from .resources.submission.client import AsyncSubmissionClient, SubmissionClient
from .resources.sysprop.client import AsyncSyspropClient, SyspropClient
from .resources.v_2.client import AsyncV2Client, V2Client


class FernIr:
    def __init__(
        self,
        *,
        environment: FernIrEnvironment = FernIrEnvironment.PROD,
        x_random_header: typing.Optional[str] = None,
        token: typing.Optional[str] = None
    ):
        self._environment = environment
        self.x_random_header = x_random_header
        self._token = token

    @cached_property
    def v_2(self) -> V2Client:
        return V2Client(environment=self._environment, x_random_header=self.x_random_header, token=self._token)

    @cached_property
    def admin(self) -> AdminClient:
        return AdminClient(environment=self._environment, x_random_header=self.x_random_header, token=self._token)

    @cached_property
    def homepage(self) -> HomepageClient:
        return HomepageClient(environment=self._environment, x_random_header=self.x_random_header, token=self._token)

    @cached_property
    def migration(self) -> MigrationClient:
        return MigrationClient(environment=self._environment, x_random_header=self.x_random_header, token=self._token)

    @cached_property
    def playlist(self) -> PlaylistClient:
        return PlaylistClient(environment=self._environment, x_random_header=self.x_random_header, token=self._token)

    @cached_property
    def problem(self) -> ProblemClient:
        return ProblemClient(environment=self._environment, x_random_header=self.x_random_header, token=self._token)

    @cached_property
    def submission(self) -> SubmissionClient:
        return SubmissionClient(environment=self._environment, x_random_header=self.x_random_header, token=self._token)

    @cached_property
    def sysprop(self) -> SyspropClient:
        return SyspropClient(environment=self._environment, x_random_header=self.x_random_header, token=self._token)


class AsyncFernIr:
    def __init__(
        self,
        *,
        environment: FernIrEnvironment = FernIrEnvironment.PROD,
        x_random_header: typing.Optional[str] = None,
        token: typing.Optional[str] = None
    ):
        self._environment = environment
        self.x_random_header = x_random_header
        self._token = token

    @cached_property
    def v_2(self) -> AsyncV2Client:
        return AsyncV2Client(environment=self._environment, x_random_header=self.x_random_header, token=self._token)

    @cached_property
    def admin(self) -> AsyncAdminClient:
        return AsyncAdminClient(environment=self._environment, x_random_header=self.x_random_header, token=self._token)

    @cached_property
    def homepage(self) -> AsyncHomepageClient:
        return AsyncHomepageClient(
            environment=self._environment, x_random_header=self.x_random_header, token=self._token
        )

    @cached_property
    def migration(self) -> AsyncMigrationClient:
        return AsyncMigrationClient(
            environment=self._environment, x_random_header=self.x_random_header, token=self._token
        )

    @cached_property
    def playlist(self) -> AsyncPlaylistClient:
        return AsyncPlaylistClient(
            environment=self._environment, x_random_header=self.x_random_header, token=self._token
        )

    @cached_property
    def problem(self) -> AsyncProblemClient:
        return AsyncProblemClient(
            environment=self._environment, x_random_header=self.x_random_header, token=self._token
        )

    @cached_property
    def submission(self) -> AsyncSubmissionClient:
        return AsyncSubmissionClient(
            environment=self._environment, x_random_header=self.x_random_header, token=self._token
        )

    @cached_property
    def sysprop(self) -> AsyncSyspropClient:
        return AsyncSyspropClient(
            environment=self._environment, x_random_header=self.x_random_header, token=self._token
        )

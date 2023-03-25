# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from ....core.remove_none_from_headers import remove_none_from_headers


class Client:
    def __init__(self, *, environment: str, x_random_header: typing.Optional[str], token: typing.Optional[str]):
        self._environment = environment
        self.x_random_header = x_random_header
        self._token = token

    def test(self) -> None:
        _response = httpx.request(
            "GET",
            self._environment,
            headers=remove_none_from_headers(
                {
                    "X-Random-Header": self.x_random_header,
                    "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                }
            ),
        )

# This file was auto-generated by Fern from our API Definition.

import typing


class Client:
    def __init__(self, *, environment: str, x_random_header: typing.Optional[str], token: typing.Optional[str]):
        self._environment = environment
        self.x_random_header = x_random_header
        self._token = token

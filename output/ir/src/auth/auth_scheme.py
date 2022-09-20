from __future__ import annotations

import typing

import pydantic

from ..commons.with_docs import WithDocs
from ..services.http.http_header import HttpHeader


class AuthScheme(pydantic.BaseModel):
    @staticmethod
    def bearer(value: WithDocs) -> AuthScheme:
        return AuthScheme(__root__=_AuthScheme(type="header"))

    @staticmethod
    def basic(value: WithDocs) -> AuthScheme:
        return AuthScheme(__root__=_AuthScheme(type="header"))

    @staticmethod
    def header(value: HttpHeader) -> AuthScheme:
        return AuthScheme(__root__=_AuthScheme(type="header"))


class _AuthScheme:
    class Bearer(WithDocs):
        type: typing.Literal["bearer"] = pydantic.Field(alias="_type")

        class Config:
            allow_population_by_field_name = True

    class Basic(WithDocs):
        type: typing.Literal["basic"] = pydantic.Field(alias="_type")

        class Config:
            allow_population_by_field_name = True

    class Header(HttpHeader):
        type: typing.Literal["header"] = pydantic.Field(alias="_type")

        class Config:
            allow_population_by_field_name = True

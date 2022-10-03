import typing

from ..commons.with_docs import WithDocs
from .auth_scheme import AuthScheme
from .auth_schemes_requirement import AuthSchemesRequirement


class ApiAuth(WithDocs):
    requirement: AuthSchemesRequirement
    schemes: typing.List[AuthScheme]

    def json(self, **kwargs) -> str:  # type: ignore
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

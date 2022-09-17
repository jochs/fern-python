import typing

from auth.auth_scheme import AuthScheme
from auth.auth_schemes_requirement import AuthSchemesRequirement
from commons.with_docs import WithDocs


class ApiAuth(WithDocs):

    requirement: AuthSchemesRequirement
    schemes: typing.List[AuthScheme]

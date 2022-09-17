import typing
from types.type_declaration import TypeDeclaration

import pydantic
from auth.api_auth import ApiAuth
from errors.error_declaration import ErrorDeclaration
from ir.fern_constants import FernConstants
from ir.services import Services


class IntermediateRepresentation(pydantic.BaseModel):

    api_name: int = pydantic.Field(alias="apiName")
    auth: ApiAuth
    types: typing.List[TypeDeclaration]
    services: Services
    errors: typing.List[ErrorDeclaration]
    constants: FernConstants

    class Config:

        allow_population_by_field_name = True

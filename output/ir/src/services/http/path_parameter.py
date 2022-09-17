from types.type_reference import TypeReference

import pydantic
from commons.string_with_all_casings import StringWithAllCasings
from commons.with_docs import WithDocs


class PathParameter(WithDocs):

    name: StringWithAllCasings
    value_type: TypeReference = pydantic.Field(alias="valueType")

    class Config:

        allow_population_by_field_name = True

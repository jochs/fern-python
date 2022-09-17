from types.type_reference import TypeReference

import pydantic


class MapType(pydantic.BaseModel):

    key_type: TypeReference = pydantic.Field(alias="keyType")
    value_type: TypeReference = pydantic.Field(alias="valueType")

    class Config:

        allow_population_by_field_name = True

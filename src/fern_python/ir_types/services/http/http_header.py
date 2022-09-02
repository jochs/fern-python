from ...commons import WithDocs, WireStringWithAllCasings
from ...types import TypeReference
import pydantic


class HttpHeader(WithDocs):
    name: WireStringWithAllCasings
    value_type: TypeReference = pydantic.Field(alias="valueType")

    class Config:
        allow_population_by_field_name = True

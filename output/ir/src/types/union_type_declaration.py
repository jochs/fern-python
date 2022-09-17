import typing
from types.single_union_type import SingleUnionType

import pydantic
from commons.wire_string_with_all_casings import WireStringWithAllCasings


class UnionTypeDeclaration(pydantic.BaseModel):

    discriminant: int
    discriminant_v_2: WireStringWithAllCasings = pydantic.Field(alias="discriminantV2")
    types: typing.List[SingleUnionType]

    class Config:

        allow_population_by_field_name = True

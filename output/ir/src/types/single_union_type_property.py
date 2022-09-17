from types.type_reference import TypeReference

import pydantic
from commons.wire_string_with_all_casings import WireStringWithAllCasings


class SingleUnionTypeProperty(pydantic.BaseModel):

    name: WireStringWithAllCasings
    type: TypeReference

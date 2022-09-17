import typing
from types.enum_value import EnumValue

import pydantic


class EnumTypeDeclaration(pydantic.BaseModel):

    values: typing.List[EnumValue]

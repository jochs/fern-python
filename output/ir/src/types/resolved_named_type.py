from types.declared_type_name import DeclaredTypeName
from types.shape_type import ShapeType

import pydantic


class ResolvedNamedType(pydantic.BaseModel):

    name: DeclaredTypeName
    shape: ShapeType

from ..commons import WithDocs, WireStringWithAllCasings
from .type_reference import TypeReference


class SingleUnionType(WithDocs):
    discriminantValue: WireStringWithAllCasings
    valueType: TypeReference

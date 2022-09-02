from ..commons import WithDocs, WireStringWithAllCasings
from .type_reference import TypeReference


class ObjectProperty(WithDocs):
    name: WireStringWithAllCasings
    valueType: TypeReference

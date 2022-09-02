from ..commons import WithDocs, WireStringWithAllCasings


class EnumValue(WithDocs):
    name: WireStringWithAllCasings
    value: str

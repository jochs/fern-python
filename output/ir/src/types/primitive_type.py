import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PrimitiveType(str, enum.Enum):

    INTEGER = "INTEGER"
    DOUBLE = "DOUBLE"
    STRING = "STRING"
    BOOLEAN = "BOOLEAN"
    LONG = "LONG"
    DATE_TIME = "DATE_TIME"
    UUID = "UUID"

    def _visit(
        self,
        integer: typing.Callable[[], T_Result],
        double: typing.Callable[[], T_Result],
        string: typing.Callable[[], T_Result],
        boolean: typing.Callable[[], T_Result],
        long: typing.Callable[[], T_Result],
        dateTime: typing.Callable[[], T_Result],
        uuid: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self.value == "INTEGER":
            integer()
        if self.value == "DOUBLE":
            double()
        if self.value == "STRING":
            string()
        if self.value == "BOOLEAN":
            boolean()
        if self.value == "LONG":
            long()
        if self.value == "DATE_TIME":
            dateTime()
        if self.value == "UUID":
            uuid()

        # the above checks are exhaustive, but this is necessary to satisfy the type checker
        raise RuntimeError()

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class SubmissionTypeEnum(str, enum.Enum):
    TEST = "TEST"

    def visit(self, test: typing.Callable[[], T_Result]) -> T_Result:
        if self.value == "TEST":
            return test()

        # the above checks are exhaustive, but this is necessary to satisfy the type checker
        raise RuntimeError()
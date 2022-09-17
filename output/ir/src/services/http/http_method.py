import enum
import typing

T_Result = typing.TypeVar("T_Result")


class HttpMethod(str, enum.Enum):

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"

    def _visit(
        self,
        get: typing.Callable[[], T_Result],
        post: typing.Callable[[], T_Result],
        put: typing.Callable[[], T_Result],
        patch: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self.value == "GET":
            get()
        if self.value == "POST":
            post()
        if self.value == "PUT":
            put()
        if self.value == "PATCH":
            patch()
        if self.value == "DELETE":
            delete()

        # the above checks are exhaustive, but this is necessary to satisfy the type checker
        raise RuntimeError()

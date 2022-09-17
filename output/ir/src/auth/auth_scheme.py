import pydantic


class AuthScheme(pydantic.BaseModel):
    @staticmethod
    def bearer() -> None:
        pass

    @staticmethod
    def basic() -> None:
        pass

    @staticmethod
    def header() -> None:
        pass

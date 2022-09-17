import pydantic


class Type(pydantic.BaseModel):
    @staticmethod
    def alias() -> None:
        pass

    @staticmethod
    def enum() -> None:
        pass

    @staticmethod
    def object() -> None:
        pass

    @staticmethod
    def union() -> None:
        pass

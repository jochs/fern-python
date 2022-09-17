import pydantic


class ContainerType(pydantic.BaseModel):
    @staticmethod
    def list() -> None:
        pass

    @staticmethod
    def map() -> None:
        pass

    @staticmethod
    def optional() -> None:
        pass

    @staticmethod
    def set() -> None:
        pass

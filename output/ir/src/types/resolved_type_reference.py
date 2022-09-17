import pydantic


class ResolvedTypeReference(pydantic.BaseModel):
    @staticmethod
    def container() -> None:
        pass

    @staticmethod
    def named() -> None:
        pass

    @staticmethod
    def primitive() -> None:
        pass

    @staticmethod
    def unknown() -> None:
        pass

    @staticmethod
    def void() -> None:
        pass

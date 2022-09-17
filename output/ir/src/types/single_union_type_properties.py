import pydantic


class SingleUnionTypeProperties(pydantic.BaseModel):
    @staticmethod
    def same_properties_as_object() -> None:
        pass

    @staticmethod
    def single_property() -> None:
        pass

    @staticmethod
    def no_properties() -> None:
        pass

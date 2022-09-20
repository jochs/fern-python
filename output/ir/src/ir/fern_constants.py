import pydantic


class FernConstants(pydantic.BaseModel):
    error_discriminant: int = pydantic.Field(alias="errorDiscriminant")
    unknown_error_discriminant_value: int = pydantic.Field(alias="unknownErrorDiscriminantValue")
    error_instance_id_key: int = pydantic.Field(alias="errorInstanceIdKey")

    class Config:
        allow_population_by_field_name = True

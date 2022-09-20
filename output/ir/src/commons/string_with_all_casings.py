import pydantic


class StringWithAllCasings(pydantic.BaseModel):
    original_value: int = pydantic.Field(alias="originalValue")
    camel_case: int = pydantic.Field(alias="camelCase")
    pascal_case: int = pydantic.Field(alias="pascalCase")
    snake_case: int = pydantic.Field(alias="snakeCase")
    screaming_snake_case: int = pydantic.Field(alias="screamingSnakeCase")

    class Config:
        allow_population_by_field_name = True

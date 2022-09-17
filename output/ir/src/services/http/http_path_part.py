import pydantic


class HttpPathPart(pydantic.BaseModel):

    path_parameter: int = pydantic.Field(alias="pathParameter")
    tail: int

    class Config:

        allow_population_by_field_name = True

from pydantic import Field, BaseModel
from typing import Literal, Union
from typing_extensions import Annotated
from ..commons import WithDocs
from .. import services


class AuthScheme(BaseModel):
    class Bearer(WithDocs):
        type: Literal["bearer"]

    class Basic(WithDocs):
        type: Literal["basic"]

    class Header(services.HttpHeader):
        type: Literal["header"]

    __root__: Annotated[
        Union[Bearer, Basic, Header],
        Field(discriminator="type"),
    ]

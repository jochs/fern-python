from typing import Literal, Optional, Union

import pydantic

from fern_python.external_dependencies import PydanticVersionCompatibility


class SDKCustomConfig(pydantic.BaseModel):
    wrapped_aliases: bool = False
    skip_formatting: bool = False
    client_class_name: Optional[str] = None
    client_filename: str = "client.py"
    include_union_utils: bool = False
    use_api_name_in_package: bool = False
    package_name: Optional[str] = None
    timeout_in_seconds: Union[Literal["infinity"], int] = 60
    flat_layout: bool = False
    version: PydanticVersionCompatibility = PydanticVersionCompatibility.Both

import pydantic


class WebSocketOperationProperties(pydantic.BaseModel):

    id: int
    operation: int
    body: int

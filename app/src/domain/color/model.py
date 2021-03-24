from pydantic import BaseModel


class Color(BaseModel):
    id: int
    name: str
    value: str

from pydantic import BaseModel


class IntDom(BaseModel):
    code: str
    name: str

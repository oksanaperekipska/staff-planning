from pydantic import BaseModel


class ArrDep(BaseModel):
    code: str
    name: str

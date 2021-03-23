from pydantic import BaseModel


class Schedule(BaseModel):
    id: int
    airport_id: int
    name: str

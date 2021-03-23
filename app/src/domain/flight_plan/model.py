from pydantic import BaseModel


class FlightPlan(BaseModel):
    id: int
    name: str

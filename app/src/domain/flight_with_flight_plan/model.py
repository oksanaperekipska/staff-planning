from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class FlightPlan(BaseModel):
    id: int
    name: str


class FlightToFlightPlan(BaseModel):
    id: int
    flight_id: Optional[str]
    flight_plan_id: Optional[int]
    start_date: Optional[datetime]
    end_date: Optional[datetime]

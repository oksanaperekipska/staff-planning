from datetime import datetime

from pydantic import BaseModel


class Task(BaseModel):
    id: int
    flight_id: str
    flight_plan_id: int
    name: str
    end_date: datetime
    start_date: datetime
    count: int
    color_id: int

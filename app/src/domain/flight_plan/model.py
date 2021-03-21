from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class FlightPlan(BaseModel):
    id: int
    name: str

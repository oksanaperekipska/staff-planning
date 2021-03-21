from typing import Optional

from pydantic import BaseModel


class Aircraft(BaseModel):
    id: int
    iata: Optional[str]
    icao: Optional[str]
    model: Optional[str]

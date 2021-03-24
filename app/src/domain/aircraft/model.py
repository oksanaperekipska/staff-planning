from pydantic import BaseModel


class Aircraft(BaseModel):
    id: int
    iata: str
    icao: str
    model: str

from pydantic import BaseModel


class Airport(BaseModel):
    id: int
    iata: str
    icao: str
    name: str
    country_id: str

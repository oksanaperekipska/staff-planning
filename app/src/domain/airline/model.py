from pydantic import BaseModel


class Airline(BaseModel):
    id: int
    iata: str
    icao: str
    name: str

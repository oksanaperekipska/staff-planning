from datetime import datetime
from typing import Optional

import uvicorn
from fastapi import FastAPI
from fastapi.params import Param, Query

from domain.flight.repository import FlightRepository

app = FastAPI()


@app.get("/", tags=["default"])
def read_root():
    return {"apiStatus": "OK", "apiVersion": "1.0.0"}


# ---- Flights -----------

@app.get("/flights/{id}", tags=["Flights"])
async def flight_get_one_by_id(id: int):
    return FlightRepository.find_one_by_id(id)


@app.get("/flights", tags=["Flights"])
async def flight_get_all_by_flight_date(flight_date_from: datetime,
                                        flight_date_to: Optional[datetime] = None,
                                        limit: Optional[int] = Query(20, le=100)):
    return FlightRepository.find_all_by_flight_date(flight_date_from, flight_date_to, limit)


# ---- Flight plan -----------

@app.get("/flight-plans", tags=["Flight plans"])
async def flight_plans(start_date: datetime,
                       end_date: Optional[datetime] = None,
                       limit: Optional[int] = Query(20, le=100)):
    return FlightRepository.find_all_by_flight_date(flight_date_from, flight_date_to, limit)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

from datetime import datetime
from typing import Optional, List

import uvicorn
from fastapi import FastAPI
from fastapi.params import Param, Query

from domain.flight.repository import FlightRepository
from domain.flight_plan.repository import FlightPlanRepository
from domain.flight_to_flight_plan.repository import FlightToFlightPlanRepository

app = FastAPI()


@app.get("/", tags=["default"])
def read_root():
    return {"apiStatus": "OK", "apiVersion": "1.0.0"}


# ---- Flights -----------

@app.get("/flights/{id}", tags=["Flights"])
async def flights_one_by_id(id: str):
    return FlightRepository.find_one_by_id(id)


@app.get("/flights/by-ids/", tags=["Flights"])
async def flights_one_by_id(id: List[str] = Query([])):
    return FlightRepository.find_all_by_ids(id)


@app.get("/flights", tags=["Flights"])
async def flights_all_by_flight_date(flight_date_from: datetime,
                                     flight_date_to: Optional[datetime] = None,
                                     limit: Optional[int] = Query(20, le=100)):
    return FlightRepository.find_all_by_flight_date(flight_date_from, flight_date_to, limit)


# ---- Flight plan -----------

@app.get("/flight-plans/{id}", tags=["Flight plans"])
async def flight_plans_one_by_id(id: int):
    return FlightPlanRepository.find_one_by_id(id)


@app.get("/flight-plans", tags=["Flight plans"])
async def flight_plans_all(offset: Optional[int] = 0, limit: Optional[int] = Query(20, le=100)):
    return FlightPlanRepository.find_all(offset, limit)


# ---- Flight to flight plan  -----------

@app.get("/flight-to-flight-plans/{id}", tags=["Flight to flight plan"])
async def flight_to_flight_plan_one_by_id(id: int):
    return FlightToFlightPlanRepository.find_one_by_id(id)


@app.get("/flight-to-flight-plans", tags=["Flight to flight plan"])
async def flight_to_flight_plan_all(offset: Optional[int] = 0, limit: Optional[int] = Query(20, le=100)):
    return FlightToFlightPlanRepository.find_all(offset, limit)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

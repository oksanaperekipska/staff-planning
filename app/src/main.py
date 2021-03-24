from datetime import datetime
from typing import Optional, List

import uvicorn
from fastapi import FastAPI
from fastapi.params import Param, Query

from domain.aircraft.repository import AircraftRepository
from domain.airline.repository import AirlineRepository
from domain.airport.repository import AirportRepository
from domain.arr_dep.repository import ArrDepRepository
from domain.color.repository import ColorRepository
from domain.country.repository import CountryRepository
from domain.flight.repository import FlightRepository
from domain.flight_plan.repository import FlightPlanRepository
from domain.flight_to_flight_plan.repository import FlightToFlightPlanRepository
from domain.int_dom.repository import IntDomRepository
from domain.schedule.repository import ScheduleRepository
from domain.service_type.repository import ServiceTypeRepository
from domain.task.repository import TaskRepository

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


# ---- Schedule -----------

@app.get("/schedules/{id}", tags=["Schedule"])
async def flight_plans_one_by_id(id: int):
    return ScheduleRepository.find_one_by_id(id)


@app.get("/schedules", tags=["Schedule"])
async def flight_plans_all(offset: Optional[int] = 0, limit: Optional[int] = Query(20, le=100)):
    return ScheduleRepository.find_all(offset, limit)


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


# ---- Aircraft  -----------

@app.get("/aircrafts/{id}", tags=["Aircraft"])
async def aircraft_one_by_id(id: int):
    return AircraftRepository.find_one_by_id(id)


@app.get("/aircrafts", tags=["Aircraft"])
async def aircraft_all(offset: Optional[int] = 0, limit: Optional[int] = Query(20, le=100)):
    return AircraftRepository.find_all(offset, limit)


# ---- Airline  -----------

@app.get("/airlines/{id}", tags=["Airline"])
async def airline_one_by_id(id: int):
    return AirlineRepository.find_one_by_id(id)


@app.get("/airlines", tags=["Airline"])
async def airline_all(offset: Optional[int] = 0, limit: Optional[int] = Query(20, le=100)):
    return AirlineRepository.find_all(offset, limit)


# ---- Airport  -----------

@app.get("/airports/{id}", tags=["Airport"])
async def airport_one_by_id(id: int):
    return AirportRepository.find_one_by_id(id)


@app.get("/airports", tags=["Airport"])
async def airport_all(offset: Optional[int] = 0, limit: Optional[int] = Query(20, le=100)):
    return AirportRepository.find_all(offset, limit)


# ---- Arrival Departure  -----------

@app.get("/arr_deps/{code}", tags=["Arrival Departure"])
async def arr_dep_one_by_code(code: str):
    return ArrDepRepository.find_one_by_code(code)


@app.get("/arr_deps", tags=["Arrival Departure"])
async def arr_dep_all(offset: Optional[int] = 0, limit: Optional[int] = Query(20, le=100)):
    return ArrDepRepository.find_all(offset, limit)


# ---- Color  -----------

@app.get("/colors/{id}", tags=["Color"])
async def color_one_by_id(id: int):
    return ColorRepository.find_one_by_id(id)


@app.get("/colors", tags=["Color"])
async def color_all(offset: Optional[int] = 0, limit: Optional[int] = Query(20, le=100)):
    return ColorRepository.find_all(offset, limit)


# ---- Country  -----------

@app.get("/countries/{id}", tags=["Country"])
async def country_one_by_id(id: int):
    return CountryRepository.find_one_by_id(id)


@app.get("/countries", tags=["Country"])
async def country_all(offset: Optional[int] = 0, limit: Optional[int] = Query(20, le=100)):
    return CountryRepository.find_all(offset, limit)


# ---- International Domestic  -----------

@app.get("/int_doms/{code}", tags=["International Domestic"])
async def int_dom_one_by_code(code: str):
    return IntDomRepository.find_one_by_code(code)


@app.get("/int_doms", tags=["International Domestic"])
async def int_dom_all(offset: Optional[int] = 0, limit: Optional[int] = Query(20, le=100)):
    return IntDomRepository.find_all(offset, limit)


# ---- Service Type  -----------

@app.get("/service_types/{code}", tags=["Service Type"])
async def service_type_one_by_code(code: str):
    return ServiceTypeRepository.find_one_by_code(code)


@app.get("/service_types", tags=["Service Type"])
async def service_type_all(offset: Optional[int] = 0, limit: Optional[int] = Query(20, le=100)):
    return ServiceTypeRepository.find_all(offset, limit)


# ---- Task  -----------

@app.get("/tasks/{id}", tags=["Task"])
async def task_one_by_code(id: int):
    return TaskRepository.find_one_by_id(id)


@app.get("/tasks", tags=["Task"])
async def task_all(offset: Optional[int] = 0, limit: Optional[int] = Query(20, le=100)):
    return TaskRepository.find_all(offset, limit)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

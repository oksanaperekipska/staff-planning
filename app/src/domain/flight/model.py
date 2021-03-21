from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Flight(BaseModel):
    id: int
    schedule_id: Optional[int]
    link_id: Optional[int]
    flight_date: Optional[datetime]
    airline_id: Optional[int]
    flight_number: Optional[int]
    arr_dep_code: Optional[str]
    flight_type_code: Optional[str]
    registration_number: Optional[str]
    aircraft_id: Optional[int]
    int_dom_code: Optional[str]
    total_passengers_count: Optional[int]
    total_c_passengers_count: Optional[int]
    total_y_passengers_count: Optional[int]
    bag_weight: Optional[int]
    cargo_weight: Optional[int]
    mail_weight: Optional[int]
    seats: Optional[int]
    parking: Optional[int]
    terminal: Optional[str]
    ori_dest_airport_id: Optional[int]
    station_airport_id: Optional[int]

from datetime import datetime
from typing import Optional

from config.database import db
from config.logs import get_module_logger
from domain.flight.model import Flight

log = get_module_logger(__name__)


class FlightPlanRepository:

    @staticmethod
    def find_one_by_id(id: str) -> Optional[FlightWi]:
        log.debug("Looking for flight with id=%s", id)
        row = db.one("SELECT * FROM flight WHERE flight.id='%(id)s'", id=id)
        return Flight(**row._asdict()) if row else None

    @staticmethod
    def find_all_by_flight_date(flight_date_from: datetime,
                                flight_date_to: datetime,
                                limit: int = 20) -> list[Flight]:
        log.debug("Looking for all flights from=%s to=%s, limit=%s", flight_date_from, flight_date_to, limit)

        where = "flight.flight_date >= %(flight_date_from)s"

        if flight_date_to:
            where = where + " AND flight.flight_date <= %(flight_date_to)s"

        rows = db.all("SELECT * FROM flight WHERE " + where + " ORDER BY flight_date LIMIT %(limit)s",
                      flight_date_from=flight_date_from,
                      flight_date_to=flight_date_to,
                      limit=limit)

        return [Flight(**row._asdict()) for row in rows]

from typing import Optional

from config.database import db
from config.logs import get_module_logger
from domain.flight_to_flight_plan.model import FlightToFlightPlan

log = get_module_logger(__name__)


class FlightToFlightPlanRepository:

    @staticmethod
    def find_one_by_id(id: int) -> Optional[FlightToFlightPlan]:
        log.debug("Looking for flight to flight plan with id=%s", id)
        row = db.one("SELECT * FROM flight_to_flight_plan WHERE id=%(id)s", id=id)
        return FlightToFlightPlan.construct(**row._asdict()) if row else None

    @staticmethod
    def find_all(offset: int = 0, limit: int = 20) -> list[FlightToFlightPlan]:
        log.debug("Looking for all flight to flight plan, offset=%s, limit=%s", offset, limit)

        rows = db.all("SELECT * FROM flight_to_flight_plan ORDER BY start_date OFFSET %(offset)s LIMIT %(limit)s",
                      offset=offset,
                      limit=limit)

        return [FlightToFlightPlan.construct(**row._asdict()) for row in rows]

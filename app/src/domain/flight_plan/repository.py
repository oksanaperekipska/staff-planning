from typing import Optional

from config.database import db
from config.logs import get_module_logger
from domain.flight_plan.model import FlightPlan

log = get_module_logger(__name__)


class FlightPlanRepository:

    @staticmethod
    def find_one_by_id(id: str) -> Optional[FlightPlan]:
        log.debug("Looking for flight plan with id=%s", id)
        row = db.one("SELECT * FROM flight_plan WHERE id='%(id)s'", id=id)
        return FlightPlan.construct(**row._asdict()) if row else None

    @staticmethod
    def find_all(limit: int = 20) -> list[FlightPlan]:
        log.debug("Looking for all flight plans, limit=%s", limit)

        rows = db.all("SELECT * FROM flight_plan ORDER BY id LIMIT %(limit)s", limit=limit)

        return [FlightPlan.construct(**row._asdict()) for row in rows]

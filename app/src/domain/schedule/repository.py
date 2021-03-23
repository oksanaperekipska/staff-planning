from typing import Optional

from config.database import db
from config.logs import get_module_logger
from domain.flight_plan.model import FlightPlan
from domain.schedule.model import Schedule

log = get_module_logger(__name__)


class ScheduleRepository:

    @staticmethod
    def find_one_by_id(id: int) -> Optional[FlightPlan]:
        log.debug("Looking for schedule with id=%s", id)
        row = db.one("SELECT * FROM schedule WHERE id=%(id)s", id=id)
        return Schedule.construct(**row._asdict()) if row else None

    @staticmethod
    def find_all(offset: int = 0, limit: int = 20) -> list[FlightPlan]:
        log.debug("Looking for all schedules, limit=%s", limit)

        rows = db.all("SELECT * FROM schedule ORDER BY id  OFFSET  %(offset)s LIMIT %(limit)s",
                      offset=offset,
                      limit=limit)

        return [Schedule.construct(**row._asdict()) for row in rows]

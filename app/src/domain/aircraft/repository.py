from typing import Optional

from config.database import db
from config.logs import get_module_logger
from domain.aircraft.model import Aircraft

log = get_module_logger(__name__)


class AircraftRepository:

    @staticmethod
    def find_one_by_id(id: int) -> Optional[Aircraft]:
        log.debug("Looking for aircraft with id=%s", id)
        row = db.one("SELECT * FROM aircraft WHERE id=%(id)s", id=id)
        return Aircraft.construct(**row._asdict()) if row else None

    @staticmethod
    def find_all(offset: int = 0, limit: int = 20) -> list[Aircraft]:
        log.debug("Looking for all aircraft, limit=%s", limit)

        rows = db.all("SELECT * FROM aircraft ORDER BY id  OFFSET  %(offset)s LIMIT %(limit)s",
                      offset=offset,
                      limit=limit)

        return [Aircraft.construct(**row._asdict()) for row in rows]

from typing import Optional

from config.database import db
from config.logs import get_module_logger
from domain.airline.model import Airline

log = get_module_logger(__name__)


class AirlineRepository:

    @staticmethod
    def find_one_by_id(id: int) -> Optional[Airline]:
        log.debug("Looking for airline with id=%s", id)
        row = db.one("SELECT * FROM airline WHERE id=%(id)s", id=id)
        return Airline.construct(**row._asdict()) if row else None

    @staticmethod
    def find_all(offset: int = 0, limit: int = 20) -> list[Airline]:
        log.debug("Looking for all airline, limit=%s", limit)

        rows = db.all("SELECT * FROM airline ORDER BY id  OFFSET  %(offset)s LIMIT %(limit)s",
                      offset=offset,
                      limit=limit)

        return [Airline.construct(**row._asdict()) for row in rows]

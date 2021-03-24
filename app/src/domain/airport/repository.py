from typing import Optional

from config.database import db
from config.logs import get_module_logger
from domain.airport.model import Airport

log = get_module_logger(__name__)


class AirportRepository:

    @staticmethod
    def find_one_by_id(id: int) -> Optional[Airport]:
        log.debug("Looking for airport with id=%s", id)
        row = db.one("SELECT * FROM airport WHERE id=%(id)s", id=id)
        return Airport.construct(**row._asdict()) if row else None

    @staticmethod
    def find_all(offset: int = 0, limit: int = 20) -> list[Airport]:
        log.debug("Looking for all airport, limit=%s", limit)

        rows = db.all("SELECT * FROM airport ORDER BY id  OFFSET  %(offset)s LIMIT %(limit)s",
                      offset=offset,
                      limit=limit)

        return [Airport.construct(**row._asdict()) for row in rows]

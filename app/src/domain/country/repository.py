from typing import Optional

from config.database import db
from config.logs import get_module_logger
from domain.country.model import Country

log = get_module_logger(__name__)


class CountryRepository:

    @staticmethod
    def find_one_by_id(id: int) -> Optional[Country]:
        log.debug("Looking for country with id=%s", id)
        row = db.one("SELECT * FROM country WHERE id=%(id)s", id=id)
        return Country.construct(**row._asdict()) if row else None

    @staticmethod
    def find_all(offset: int = 0, limit: int = 20) -> list[Country]:
        log.debug("Looking for all country, limit=%s", limit)

        rows = db.all("SELECT * FROM country ORDER BY id  OFFSET  %(offset)s LIMIT %(limit)s",
                      offset=offset,
                      limit=limit)

        return [Country.construct(**row._asdict()) for row in rows]

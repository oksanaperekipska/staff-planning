from typing import Optional

from config.database import db
from config.logs import get_module_logger
from domain.arr_dep.model import ArrDep

log = get_module_logger(__name__)


class ArrDepRepository:

    @staticmethod
    def find_one_by_code(code: str) -> Optional[ArrDep]:
        log.debug("Looking for arr_dep with code=%s", code)
        row = db.one("SELECT * FROM arr_dep WHERE code=%(code)s", code=code)
        return ArrDep.construct(**row._asdict()) if row else None

    @staticmethod
    def find_all(offset: int = 0, limit: int = 20) -> list[ArrDep]:
        log.debug("Looking for all arr_dep, limit=%s", limit)

        rows = db.all("SELECT * FROM arr_dep ORDER BY code  OFFSET  %(offset)s LIMIT %(limit)s",
                      offset=offset,
                      limit=limit)

        return [ArrDep.construct(**row._asdict()) for row in rows]

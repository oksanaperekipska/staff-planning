from typing import Optional

from config.database import db
from config.logs import get_module_logger
from domain.int_dom.model import IntDom

log = get_module_logger(__name__)


class IntDomRepository:

    @staticmethod
    def find_one_by_code(code: str) -> Optional[IntDom]:
        log.debug("Looking for int_dom with code=%s", code)
        row = db.one("SELECT * FROM int_dom WHERE code=%(code)s", code=code)
        return IntDom.construct(**row._asdict()) if row else None

    @staticmethod
    def find_all(offset: int = 0, limit: int = 20) -> list[IntDom]:
        log.debug("Looking for all int_dom, limit=%s", limit)

        rows = db.all("SELECT * FROM int_dom ORDER BY code  OFFSET  %(offset)s LIMIT %(limit)s",
                      offset=offset,
                      limit=limit)

        return [IntDom.construct(**row._asdict()) for row in rows]

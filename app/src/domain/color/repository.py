from typing import Optional

from config.database import db
from config.logs import get_module_logger
from domain.color.model import Color

log = get_module_logger(__name__)


class ColorRepository:

    @staticmethod
    def find_one_by_id(id: int) -> Optional[Color]:
        log.debug("Looking for color with id=%s", id)
        row = db.one("SELECT * FROM color WHERE id=%(id)s", id=id)
        return Color.construct(**row._asdict()) if row else None

    @staticmethod
    def find_all(offset: int = 0, limit: int = 20) -> list[Color]:
        log.debug("Looking for all color, limit=%s", limit)

        rows = db.all("SELECT * FROM color ORDER BY id  OFFSET  %(offset)s LIMIT %(limit)s",
                      offset=offset,
                      limit=limit)

        return [Color.construct(**row._asdict()) for row in rows]

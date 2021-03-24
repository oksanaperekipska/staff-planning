from typing import Optional

from config.database import db
from config.logs import get_module_logger
from domain.service_type.model import ServiceType

log = get_module_logger(__name__)


class ServiceTypeRepository:

    @staticmethod
    def find_one_by_code(code: str) -> Optional[ServiceType]:
        log.debug("Looking for service_type with code=%s", code)
        row = db.one("SELECT * FROM service_type WHERE code=%(code)s", code=code)
        return ServiceType.construct(**row._asdict()) if row else None

    @staticmethod
    def find_all(offset: int = 0, limit: int = 20) -> list[ServiceType]:
        log.debug("Looking for all service_type, limit=%s", limit)

        rows = db.all("SELECT * FROM service_type ORDER BY code  OFFSET  %(offset)s LIMIT %(limit)s",
                      offset=offset,
                      limit=limit)

        return [ServiceType.construct(**row._asdict()) for row in rows]

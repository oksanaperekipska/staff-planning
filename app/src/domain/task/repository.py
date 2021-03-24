from typing import Optional

from config.database import db
from config.logs import get_module_logger
from domain.task.model import Task

log = get_module_logger(__name__)


class TaskRepository:

    @staticmethod
    def find_one_by_id(id: int) -> Optional[Task]:
        log.debug("Looking for task with id=%s", id)
        row = db.one("SELECT * FROM task WHERE id=%(id)s", id=id)
        return Task.construct(**row._asdict()) if row else None

    @staticmethod
    def find_all(offset: int = 0, limit: int = 20) -> list[Task]:
        log.debug("Looking for all task, limit=%s", limit)

        rows = db.all("SELECT * FROM task ORDER BY id  OFFSET  %(offset)s LIMIT %(limit)s",
                      offset=offset,
                      limit=limit)

        return [Task.construct(**row._asdict()) for row in rows]

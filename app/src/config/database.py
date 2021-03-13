import logging

from postgres import Postgres
import os

log = logging.getLogger(__name__)


DB_HOST = os.environ.get('DB_HOST', '127.0.0.1')
DB_PORT = os.environ.get('DB_PORT', '5432')
DB_USER = os.environ.get('DB_USER', 'staff-planning')
DB_PASS = os.environ.get('DB_PASS', 'staff-planning')
DB_NAME = os.environ.get('DB_NAME', DB_USER)

DB_URL = os.environ.get('DB_URL', f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

log.info(f"Database connecting. Host: %s, port: %s, database: %s, username: %s", DB_HOST, DB_PORT, DB_NAME, DB_USER)
db = Postgres(DB_URL)

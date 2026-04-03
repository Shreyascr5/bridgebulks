# deps.py - use the centralised get_db from db.py
# The old version imported from "db" (missing "app." prefix) which crashes on Linux.
from app.db import get_db  # noqa: F401 - re-exported for any file that imports from app.deps

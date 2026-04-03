# Thin wrapper - re-exports redis_client from cache.py for backward compatibility.
from app.cache import redis_client  # noqa: F401

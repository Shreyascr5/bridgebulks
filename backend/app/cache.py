import os
import redis

REDIS_URL = os.getenv("REDIS_URL", "")

# Redis is optional - if not configured, cache operations are no-ops.
# This prevents the backend from crashing on Render free tier (no Redis).
redis_client = None

if REDIS_URL:
    try:
        redis_client = redis.from_url(REDIS_URL, decode_responses=True)
        redis_client.ping()
    except Exception as e:
        print(f"[cache] Redis not available: {e}. Continuing without cache.")
        redis_client = None
else:
    print("[cache] REDIS_URL not set. Running without Redis cache.")

try:
    import redis
except Exception:
    redis = None

# Use a module-level client when Redis is available. Callers must handle None.
redis_client = (
    redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
    if redis
    else None
)

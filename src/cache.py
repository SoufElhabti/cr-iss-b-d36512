import time

_CACHE = {}

def get(key, ttl=60):
    v = _CACHE.get(key)
    if v and time.time() - v[1] < ttl:
        return v[0]
    return None

def put(key, value):
    _CACHE[key] = (value, time.time())

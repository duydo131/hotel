from config.celery import app
from core.utils import GenCachePrefixKey
import redis

@app.task
def update_cache(path):
    if path is None:
        return None
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    for key in r.scan_iter(f"*{path}*".format(path=path)):
        r.delete(key)


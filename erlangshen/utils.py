import redis


class Storage:

    def __init__(self):
        self.db = redis.StrictRedis(decode_responses=True)

    def get(self, key):
        return self.db.get(key)

    def set(self, key, value):
        self.db.set(key, value)

    def clear(self, key):
        self.db.delete(key)

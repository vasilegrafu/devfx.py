
class MemoryCache(object):
    __storage = { }

    @classmethod
    def set(cls, key, value):
        cls.__storage[key] = value

    @classmethod
    def remove(cls, key):
        cls.__storage.pop(key)

    @classmethod
    def exists(cls, key):
        return key in cls.__storage.keys()

    @classmethod
    def get(cls, key):
        return cls.__storage[key]

    @classmethod
    def intercept(cls, key, value):
        if(not cls.exists(key)):
            cls.set(key, value)
        return cls.get(key)

    
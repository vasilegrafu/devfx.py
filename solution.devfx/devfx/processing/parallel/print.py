from .lock import Lock

__lock = Lock()

__print = print

def print(*args, **kwargs):
    with __lock:
        __print(*args, **kwargs)
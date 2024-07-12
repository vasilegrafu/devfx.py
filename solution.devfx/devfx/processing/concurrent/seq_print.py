from .lock import Lock

__lock = Lock()

def print(*args, **kwargs):
    with __lock:
        print(*args, **kwargs)
from .lock import Lock

__lock = Lock()

def seq_print(*args, **kwargs):
    with __lock:
        print(*args, **kwargs)
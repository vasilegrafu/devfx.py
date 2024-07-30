from threading import Thread
from queue import Queue

# ----------------------------------------------------------------
# Example:
# def fn(item):
#     print(item)
#
# iterable = range(100)
# n = 10
# parallel_for(iterable, n, fn)
# ----------------------------------------------------------------

def __worker(queue, fn):
    while True:
        item = queue.get()
        if item is None:
            break
        try:
            fn(item)
        finally:
            queue.task_done()

def parallel_for(iterable, n, fn):
    # Create a queue
    queue = Queue()

    # Create worker threads
    threads = []

    # Enqueue all items
    for item in iterable:
        queue.put(item)

    # Start worker threads
    for _ in range(n):
        thread = Thread(target=__worker, args=(queue, fn))
        thread.start()
        threads.append(thread)

    # Block until all tasks are done
    queue.join()

    # Stop the worker threads
    for _ in range(n):
        queue.put(None)

    # Wait for all worker threads to stop
    for thread in threads:
        thread.join()

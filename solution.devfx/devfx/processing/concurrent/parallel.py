from threading import Thread
from queue import Queue

def __worker(queue):
    while True:
        fn = queue.get()
        if fn is None:
            break
        try:
            fn()
        finally:
            queue.task_done()

def parallel(fns, n=None):
    # Create a queue
    queue = Queue()

    # Create worker threads
    threads = []

    # Enqueue all items
    for fn in fns:
        queue.put(fn)

    if(n is None):
        n = len(fns)

    # Start worker threads
    for _ in range(n):
        thread = Thread(target=__worker, args=(queue,))
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

# # ----------------------------------------------------------------
# # Example:
# def fn1():
#     print(1)

# def fn2():
#     print(2)

# def fn3():
#     print(3)

# def fn4():
#     print(4)

# parallel([fn1, fn2, fn3, fn4], 2)
# # ----------------------------------------------------------------
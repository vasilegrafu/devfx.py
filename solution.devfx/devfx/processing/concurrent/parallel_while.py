from threading import Thread
import time

def __worker(fn, execution_interval):
    while True:
        try:
            fn()
        finally:
            if(execution_interval is not None):
                time.sleep(execution_interval)

def parallel_while(fn, execution_interval=None):
    thread = Thread(target=__worker, args=(fn, execution_interval))
    thread.start()

# # ----------------------------------------------------------------
# # Example:
# def fn():
#     print(1)
#     time.sleep(1)
#
# parallel_while(fn, 1)

# time.sleep(5)
# # ----------------------------------------------------------------

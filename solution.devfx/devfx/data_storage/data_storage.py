from threading import Thread
from threading import RLock
import time
from contextlib import contextmanager

class DataStorage(object):
    __data_storage = {}
    __reload_threads_storage = {}
    __update_threads_storage = {}

    __key_locks = {}
    __get_key_lock_lock = RLock()
    @contextmanager
    def __get_key_lock(key):
        DataStorage.__get_key_lock_lock.acquire()
        try:
            if(key not in DataStorage.__key_locks):
                DataStorage.__key_locks[key] = RLock()
            key_lock = DataStorage.__key_locks[key]
        finally:
            DataStorage.__get_key_lock_lock.release()
        
        key_lock.acquire()
        try:
            yield
        finally:
            key_lock.release()

    @staticmethod
    def __execute_reload(key, reload_fn, refresh_interval=None):
        while True:
            try:
                if(refresh_interval is not None):
                    time.sleep(refresh_interval)
                data = reload_fn()
                with DataStorage.__get_key_lock(key):
                    DataStorage.__data_storage[key] = data
            except Exception as e:
                raise e
            finally:
                pass

    @staticmethod
    def __execute_update(key, update_fn, refresh_interval=None):
        while True:
            try:
                if(refresh_interval is not None):
                    time.sleep(refresh_interval)
                data = DataStorage.__data_storage[key]
                data = update_fn(data)
                with DataStorage.__get_key_lock(key):
                    DataStorage.__data_storage[key] = data
            except Exception as e:
                raise e
            finally:
                pass

    @staticmethod
    def get(key, load_fn, reload_fn=None, update_fn=None, refresh_interval=None):  
        with DataStorage.__get_key_lock(key):
            if(key not in DataStorage.__data_storage):
                try:
                    data = load_fn()
                    DataStorage.__data_storage[key] = data
                    if(reload_fn is not None):
                        DataStorage.__reload_threads_storage[key] = Thread(target=DataStorage.__execute_reload, args=(key, reload_fn, refresh_interval))
                        DataStorage.__reload_threads_storage[key].daemon = True
                        DataStorage.__reload_threads_storage[key].start()
                    if(update_fn is not None):
                        DataStorage.__update_threads_storage[key] = Thread(target=DataStorage.__execute_update, args=(key, update_fn, refresh_interval))
                        DataStorage.__update_threads_storage[key].daemon = True
                        DataStorage.__update_threads_storage[key].start()
                finally:
                    pass
            data = DataStorage.__data_storage[key]
            return data

    @staticmethod
    def has_data(key):
        with DataStorage.__get_key_lock(key):
            return key in DataStorage.__data_storage
        
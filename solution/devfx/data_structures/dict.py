import numpy as np
import collections as colls
import devfx.core as core
from .comparable import comparable

class dict(colls.UserDict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
    def __len__(self): 
        return super().__len__()

    def __getitem__(self, key):
        return super().__getitem__(comparable(key))

    def __setitem__(self, key, item): 
        super().__setitem__(comparable(key), item)

    def __delitem__(self, key): 
        super().__delitem__(comparable(key))

    def __iter__(self):
        return iter(comparable.value for comparable in self.data)

    def __contains__(self, key):
        super().__contains__(comparable(key))
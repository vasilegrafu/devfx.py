import json as json
from ..core import GlobalStorage
from ..core import is_instance
from ..exceptions import NotFoundError

class Configuration(object):
    def __init__(self, config_node):
        self.__config_node = config_node

    def __getitem__(self, key):    
        config_node = self.__config_node    
        if ':' in key:
            keys = key.split(':')
            for k in keys:
                if(k in config_node):
                    config_node = config_node[k]
                else:
                    raise NotFoundError(f"Key '{key}' not found in configuration.")
                
            if(is_instance(config_node, dict)):
                return Configuration(config_node)
            else:
                return config_node
        else:
            if(key in config_node):
                if(is_instance(config_node[key], dict)):
                    return Configuration(config_node[key])
                else:
                    return config_node[key]
            else:
                raise NotFoundError(f"Key '{key}' not found in configuration.")
        
    @classmethod
    def load(cls, config_file_path):
        with open(config_file_path) as config_file:
            configuration = Configuration(json.load(config_file))
            GlobalStorage.set(f'7fae92dc-fcd4-4a98-8d97-4605189335e8', configuration)
            return configuration
        
    @classmethod
    def get(cls, key=None):
        configuration = GlobalStorage.get(f'7fae92dc-fcd4-4a98-8d97-4605189335e8')
        if(key is not None):
            return configuration[key]
        return configuration







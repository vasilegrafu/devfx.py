import json as json
from ..core import GlobalStorage
from ..core import is_instance

class Configuration(object):
    def __init__(self, config_node):
        self.__config_node = config_node

    def __getitem__(self, key):
        config_node_value = self.__config_node[key]
        if(is_instance(config_node_value, dict)):
            return Configuration(config_node_value)
        else:
            return config_node_value
        
    @classmethod
    def load(cls, config_file_path):
        with open(config_file_path) as config_file:
            configuration = Configuration(json.load(config_file))
            GlobalStorage.set(f'7fae92dc-fcd4-4a98-8d97-4605189335e8', configuration)
            return configuration
        
    @classmethod
    def get(cls):
        configuration = GlobalStorage.get(f'7fae92dc-fcd4-4a98-8d97-4605189335e8')
        return configuration





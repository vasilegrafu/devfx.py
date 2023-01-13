import json as json
from ..core import is_instance

class ConfigNode(object):
    def __init__(self, config_node):
        self.__config_node = config_node

    def __getitem__(self, key):
        config_node_value = self.__config_node[key]
        if(is_instance(config_node_value, dict)):
            return ConfigNode(config_node_value)
        else:
            return config_node_value

class ConfigManager(object):
    def __class_getitem__(cls, key):
        with open('config.json') as config_file:
            config_root_node = json.load(config_file)
            return ConfigNode(config_root_node)[key]

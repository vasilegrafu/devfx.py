import json as json
from ..core import is_instance

class ConfigNodeManager(object):
    def __init__(self, config_node):
        self.__config_node = config_node

    def __getitem__(self, key):
        config_node = self.__config_node[key]
        if(is_instance(config_node, dict)):
            return ConfigNodeManager(config_node)
        else:
            return config_node

class ConfigManager(object):
    def __class_getitem__(cls, key):
        with open('config.json') as config_file:
            config_root_node = json.load(config_file)
            return ConfigNodeManager(config_root_node)[key]

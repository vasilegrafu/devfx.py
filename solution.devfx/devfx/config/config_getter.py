from ..core import is_instance

class ConfigGetter(object):
    def __init__(self, config_node):
        self.__config_node = config_node

    def __getitem__(self, key):
        config_node_value = self.__config_node[key]
        if(is_instance(config_node_value, dict)):
            return ConfigGetter(config_node_value)
        else:
            return config_node_value


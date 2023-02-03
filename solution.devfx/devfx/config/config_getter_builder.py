import json as json
from .config_getter import ConfigGetter

class ConfigGetterBuilder(object):
    @staticmethod
    def build(config_file_path):
        with open(config_file_path) as config_file:
            config_root_node = json.load(config_file)
            return ConfigGetter(config_root_node)

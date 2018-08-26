
class AttributesManager(object):
    def __init__(self, attributes):
        self.__attributes = attributes

    """----------------------------------------------------------------
    """
    def __len__(self):
        return len(self.__attributes)

    """----------------------------------------------------------------
    """
    def set(self, name, value):
        self.__attributes[name] = value

    def __setitem__(self, name, value):
        return self.set(name, value)

    def get(self, name):
        return self.__attributes[name]

    def __getitem__(self, name):
        return self.get(name)

    def exists(self, name):
        return name in self.__attributes.keys()

    def remove(self, name):
        del self.__attributes[name]
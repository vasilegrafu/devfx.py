class persistentvariable(object):
    __storage__ = {}

    @staticmethod
    def __new__(cls, name, constructor):
        if(name not in persistentvariable.__storage__):
            persistentvariable.__storage__[name] = constructor()
        variable = persistentvariable.__storage__[name]
        return variable
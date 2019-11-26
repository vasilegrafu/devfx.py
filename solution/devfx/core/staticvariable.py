class staticvariable(object):
    __persister__ = {}

    @staticmethod
    def __new__(cls, id, constructor):
        if(id not in staticvariable.__persister__):
            variable = constructor()
            staticvariable.__persister__[id] = variable
        variable = staticvariable.__persister__[id]
        return variable
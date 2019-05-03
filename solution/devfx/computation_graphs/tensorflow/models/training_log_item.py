import devfx.exceptions as exps
import devfx.reflection as refl

"""------------------------------------------------------------------------------------------------
"""
class TrainingLogItem(object):
    def __init__(self, nr, time_elapsed, time_delta, iteration, epoch):
        self.__attr_list__ = []

        self.nr = int(nr)
        self.time_elapsed = time_elapsed
        self.time_delta = time_delta
        self.iteration = iteration
        self.epoch = epoch

    def __setattr__(self, name, value):
        if(name == '__attr_list__'):
            super().__setattr__(name, value)
        else:
            super().__setattr__(name, value)
            self.__attr_list__.append((name, value))

    def __str__(self):
        name_value_list = []
        for attr in self.__attr_list__:
            name = attr[0]
            value = attr[1]

            if(name == 'time_elapsed'):
                name_value_list.append("{name}={value}".format(name=name, value=value)[:-3])
            elif(name == 'time_delta'):
                name_value_list.append("{name}={value}".format(name=name, value=value)[:-3])
            elif (name == 'iteration'):
                name_value_list.append("{name}={value}".format(name=name, value=value))
            elif (name == 'epoch'):
                name_value_list.append("{name}={value:.3f}".format(name=name, value=value))
            elif(value is None):
                name_value_list.append("{name}={value}".format(name=name, value=None))
            elif(refl.is_typeof(value, str)):
                name_value_list.append("{name}={value}".format(name=name, value=value))
            elif (refl.is_typeof(value, int)):
                name_value_list.append("{name}={value}".format(name=name, value=value))
            else:
                try:
                    value = float(value)
                    name_value_list.append("{name}={value:.6f}".format(name=name, value=value))
                except:
                    name_value_list.append("{name}={value}".format(name=name, value=value))
        return ', '.join(name_value_list)

    def __repr__(self):
        raise exps.NotSupportedError()

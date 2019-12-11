import devfx.core as core
import devfx.mathematics as math

"""------------------------------------------------------------------------------------------------
"""
class distribution_algebra_operation_node(object):
    def __init__(self, sample_fn):
        self.__sample_fn = sample_fn

    """------------------------------------------------------------------------------------------------
    """
    sample_size = 1024*1024

    def sample(self, size=sample_size):
        return self.__sample_fn(size)

    """ ---------------- unary ----------------
    """
    def _unary_operation(self, operation):
        return distribution_algebra_operation_node(lambda size: getattr(self.sample(size), operation)())

    def __neg__(self):
        return self._unary_operation("__neg__")

    def __pos__(self):
        return self._unary_operation("__pos__")

    """ ---------------- binary ----------------
    """
    def __binary_operation(self, operation, other):
        if (core.is_typeof(other, distribution_algebra_operation_node)):
            return distribution_algebra_operation_node(lambda size: getattr(self.sample(size), operation)(other.sample(size)))
        else:
            return distribution_algebra_operation_node(lambda size: getattr(self.sample(size), operation)(other))

    def __add__(self, other):
        return self.__binary_operation("__add__", other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self.__binary_operation("__sub__", other)

    def __rsub__(self, other):
        return self.__rsub__(other)

    def __mul__(self, other):
        return self.__binary_operation("__mul__", other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __floordiv__(self, other):
        return self.__binary_operation("__floordiv__", other)

    def __rfloordiv__(self, other):
        return self.__floordiv__(other)

    def __truediv__(self, other):
        return self.__binary_operation("__truediv__", other)

    def __rdiv__(self, other):
        return self.__truediv__(other)

    def __mod__(self, other):
        return self.__binary_operation("__mod__", other)

    def __rmod__(self, other):
        return self.__mod__(other)

    def __pow__(self, other):
        return self.__binary_operation("__pow__", other)

    def __rpow__(self, other):
        return self.__pow__(other)

    def __iadd__(self, other):
        return self.__binary_operation("__iadd__", other)

    def __isub__(self, other):
        return self.__binary_operation("__isub__", other)

    def __imul__(self, other):
        return self.__binary_operation("__imul__", other)

    def __ifloordiv__(self, other):
        return self.__binary_operation("__ifloordiv__", other)

    def __idiv__(self, other):
        return self.__binary_operation("__idiv__", other)

    def __imod__(self, other):
        return self.__binary_operation("__imod__", other)

    def __ipow__(self, other):
        return self.__binary_operation("__ipow__", other)


    """ ---------------- functions ----------------
    """

    """ square
    """
    def sqr(self):
        return distribution_algebra_operation_node(lambda size: math.sqr(self.sample(size)))

    """ cubic
    """
    def cb(self):
        return distribution_algebra_operation_node(lambda size: math.cb(self.sample(size)))

    """ exponential
    """
    def exp(self, a):
        return distribution_algebra_operation_node(lambda size: math.exp(a, self.sample(size)))

    def exp2(self):
        return distribution_algebra_operation_node(lambda size: math.exp2(self.sample(size)))

    def exp10(self):
        return distribution_algebra_operation_node(lambda size: math.exp10(self.sample(size)))

    def expe(self):
        return distribution_algebra_operation_node(lambda size: math.expe(self.sample(size)))

    """ power
    """
    def pow(self, a):
        return distribution_algebra_operation_node(lambda size: math.pow(self.sample(size), a))

    def pow2(self):
        return distribution_algebra_operation_node(lambda size: math.pow2(self.sample(size)))

    def pow10(self):
        return distribution_algebra_operation_node(lambda size: math.pow10(self.sample(size)))

    def powe(self):
        return distribution_algebra_operation_node(lambda size: math.powe(self.sample(size)))

    def sqrt(self):
        return distribution_algebra_operation_node(lambda size: math.sqrt(self.sample(size)))

    def cbrt(self):
        return distribution_algebra_operation_node(lambda size: math.cbrt(self.sample(size)))

    """ logarithmic
    """
    def log(self, b):
        return distribution_algebra_operation_node(lambda size: math.log(self.sample(size), b))

    def log2(self):
        return distribution_algebra_operation_node(lambda size: math.log2(self.sample(size)))

    def log10(self):
        return distribution_algebra_operation_node(lambda size: math.log10(self.sample(size)))

    def loge(self):
        return distribution_algebra_operation_node(lambda size: math.loge(self.sample(size)))

    """ trigonometric
    """
    def sin(self):
        return distribution_algebra_operation_node(lambda size: math.sin(self.sample(size)))

    def cos(self):
        return distribution_algebra_operation_node(lambda size: math.cos(self.sample(size)))

    def tan(self):
        return distribution_algebra_operation_node(lambda size: math.tan(self.sample(size)))

    """ miscellaneous
    """
    def sgn(self):
        return distribution_algebra_operation_node(lambda size: math.sgn(self.sample(size)))

    def floor(self):
        return distribution_algebra_operation_node(lambda size: math.floor(self.sample(size)))

    def ceil(self):
        return distribution_algebra_operation_node(lambda size: math.ceil(self.sample(size)))

    def round(self, decimals=None):
        return distribution_algebra_operation_node(lambda size: math.round(self.sample(size), decimals=decimals))

    def abs(self):
        return distribution_algebra_operation_node(lambda size: math.abs(self.sample(size)))

    """ function
    """
    def function(self, fn):
        return distribution_algebra_operation_node(lambda size: fn(self.sample(size)))
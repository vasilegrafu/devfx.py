"""----------------------------------------------------------
"""
from . import errors

"""----------------------------------------------------------
"""
from .types import bool
from .types import int8
from .types import int16
from .types import int32
from .types import int64
from .types import uint8
from .types import uint16
from .types import float16
from .types import float32
from .types import float64
from .types import string

from .types import is_typeof
from .types import is_typeof_bool
from .types import is_typeof_int8
from .types import is_typeof_int16
from .types import is_typeof_int32
from .types import is_typeof_int64
from .types import is_typeof_uint8
from .types import is_typeof_uint16
from .types import is_typeof_float16
from .types import is_typeof_float32
from .types import is_typeof_float64
from .types import is_typeof_string

from .types import cast
from .types import cast_to_bool
from .types import cast_to_int8
from .types import cast_to_int16
from .types import cast_to_int32
from .types import cast_to_int64
from .types import cast_to_uint8
from .types import cast_to_uint16
from .types import cast_to_float16
from .types import cast_to_float32
from .types import cast_to_float64
from .types import cast_to_string

"""----------------------------------------------------------
"""
from .tensors import convert_to_tensor

from .tensors import constant
from .tensors import fill

from .tensors import zeros
from .tensors import zeros_like
from .tensors import ones
from .tensors import ones_like

from .tensors import linspace
from .tensors import range

from .tensors import random_uniform
from .tensors import random_normal
from .tensors import random_truncated_normal

from .tensors import one_hot

from .tensors import shape
from .tensors import rank
from .tensors import size

from .tensors import reshape

from .tensors import tile
from .tensors import slice
from .tensors import split
from .tensors import stack
from .tensors import unstack
from .tensors import concatenate

from .tensors import where

from .tensors import equal
from .tensors import not_equal
from .tensors import less
from .tensors import less_equal
from .tensors import greater
from .tensors import greater_equal

"""----------------------------------------------------------
"""
from .variables import Variable

"""----------------------------------------------------------
"""
from .initializers import zeros_initializer
from .initializers import ones_initializer
from .initializers import constant_initializer

from .initializers import random_uniform_initializer
from .initializers import random_normal_initializer

from .initializers import xavier_glorot_random_uniform_initializer
from .initializers import xavier_glorot_random_normal_initializer
from .initializers import xavier_glorot_random_truncated_normal_initializer


"""----------------------------------------------------------
"""
from .mathematics import is_finite
from .mathematics import is_inf
from .mathematics import is_neginf
from .mathematics import is_posinf
from .mathematics import is_nan

from .mathematics import clip_by_value
from .mathematics import clip_by_inf
from .mathematics import clip_by_neginf_max
from .mathematics import clip_by_min_posinf

from .mathematics import add
from .mathematics import add_n
from .mathematics import subtract
from .mathematics import multiply
from .mathematics import scalar_multiply
from .mathematics import divide
from .mathematics import mod

from .mathematics import min
from .mathematics import max
from .mathematics import argmin
from .mathematics import argmax

from .mathematics import cumulative_sum
from .mathematics import cumulative_product

from .mathematics import reduce_sum
from .mathematics import reduce_prod
from .mathematics import reduce_min
from .mathematics import reduce_max
from .mathematics import reduce_all
from .mathematics import reduce_any

from .mathematics import reduce_mean
from .mathematics import reduce_var
from .mathematics import reduce_std

from .mathematics import sign
from .mathematics import reciprocal
from .mathematics import round
from .mathematics import ceil
from .mathematics import floor

from .mathematics import identity
from .mathematics import exp
from .mathematics import log
from .mathematics import abs
from .mathematics import sqrt
from .mathematics import square
from .mathematics import pow
from .mathematics import sin
from .mathematics import cos
from .mathematics import arcsin
from .mathematics import arccos
from .mathematics import tan
from .mathematics import arctan

from .mathematics import logical_not
from .mathematics import logical_and
from .mathematics import logical_or
from .mathematics import logical_xor

from .mathematics import matrix_eye
from .mathematics import matrix_determinant
from .mathematics import matrix_transpose
from .mathematics import matrix_inverse
from .mathematics import matrix_multiply

from .mathematics import tensordot
from .mathematics import einsum

from .mathematics import iverson
from .mathematics import macaulay
from .mathematics import kronecker

"""----------------------------------------------------------
"""
from .devices import device

"""----------------------------------------------------------
"""
from .control_flow import condition
from .control_flow import case
from .control_flow import while_loop

from .control_flow import control_dependencies

"""----------------------------------------------------------
"""
from . import diagnostics

"""----------------------------------------------------------
"""
from . import logging

"""----------------------------------------------------------
"""
from . import train

"""----------------------------------------------------------
"""
from .models import Model
from .models import model_executer





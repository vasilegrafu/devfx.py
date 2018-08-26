"""----------------------------------------------------------
"""
from .distributions import distribution

from .distributions import ddiscrete
from .distributions import ddiscrete_builder
from .distributions import dcontinuous
from .distributions import dcontinuous_builder

from .distributions import bernoulli
from .distributions import binomial
from .distributions import poisson
from .distributions import exponential
from .distributions import erlang
from .distributions import gamma
from .distributions import geometrick1
from .distributions import geometrick0
from .distributions import negbinomial
from .distributions import uniform
from .distributions import beta
from .distributions import normal
from .distributions import halfnormal
from .distributions import chisquare
from .distributions import student
from .distributions import lognormal
from .distributions import logistic

from .distributions import empirical
from .distributions import kde

"""----------------------------------------------------------
"""
from .series import mean
from .series import avg
from .series import median
from .series import mode

from .series import cov
from .series import corr

from .series import mad
from .series import S2
from .series import S
from .series import var
from .series import stddev
from .series import min
from .series import max
from .series import range
from .series import percentile
from .series import Q1
from .series import Q2
from .series import Q3
from .series import IQR

from .series import outliersNx_limits
from .series import is_outlierNx
from .series import lolNx
from .series import uolNx
from .series import outliers_limits
from .series import is_outlier
from .series import lol
from .series import uol
from .series import outliers2x_limits
from .series import is_outlier2x
from .series import lol2x
from .series import uol2x
from .series import outliers4x_limits
from .series import is_outlier4x
from .series import lol4x
from .series import uol4x
from .series import outliers8x_limits
from .series import is_outlier8x
from .series import lol8x
from .series import uol8x

from .series import skew
from .series import kurtosis

"""----------------------------------------------------------
"""
from .estimators import ci
from .estimators import pi
from .estimators import dhistogram
from .estimators import cdhistogram

"""----------------------------------------------------------
"""
from .tests import pvalue
from .tests import htest
from .tests import gofftest


"""----------------------------------------------------------
"""
from .regression import trend
from .regression import normalized_trend

"""----------------------------------------------------------
"""
from .preprocessing import one_hot

from .preprocessing import Normalizer
from .preprocessing import StandardScaler
from .preprocessing import MinMaxScaler
from .preprocessing import LabelEncoder
from .preprocessing import LabelBinarizer

from .preprocessing import Slicer
from .preprocessing import Splitter
from .preprocessing import RandomSelector

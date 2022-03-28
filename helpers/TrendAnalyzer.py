import numpy as np
import pymannkendall as mk
from scipy.stats import linregress


def trend_polynomial_regression(extrema, window):
    result = np.polyfit(extrema.index, extrema.extrema, window)
    slope = float(result[-2])

    return slope


def trend_linear_regression(extrema):
    result = linregress(extrema.index, extrema.extrema)
    slope = float(result[0])

    return slope


# Mann-Kendall Trend
def trend_mannkendall(extrema):
    result = mk.original_test(extrema.extrema)

    return result.trend

import numpy as np
import pymannkendall as mk
from scipy.stats import linregress

import config.Text


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


def find_good_start(minima_maxima, start):
    _start = start
    trend = trend_mannkendall(minima_maxima)

    if trend == config.Text.increasing and minima_maxima[config.Text.type][start] == config.Text.maxima:
        _start = 1
    elif trend == config.Text.decreasing and minima_maxima[config.Text.type][start] == config.Text.minima:
        _start = 1

    return _start

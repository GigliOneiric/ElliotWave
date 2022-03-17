import numpy as np
import pandas as pd
from scipy.signal import argrelextrema


def minmax(df, window):
    # Get minima/maxima for the given window-size
    extrema = _get_extrema(df, window)

    # Get the highest maxima/ the lowest minima

    extrema = _group_extrema(extrema)

    # Clean the dataframe

    extrema = _clean_extrema(extrema)

    # Reorganize dataframe

    extrema = _reorganize_extrema(extrema)

    return extrema


def _get_extrema(df, window):
    close = df.close.values
    close_index = df.close.index

    minima_index = argrelextrema(close, np.less, order=window)
    minima_index = minima_index[0]

    maxima_index = argrelextrema(close, np.greater, order=window)
    maxima_index = maxima_index[0]

    minima = pd.DataFrame({'date': close_index[minima_index], 'minima': close[minima_index]})
    maxima = pd.DataFrame({'date': close_index[maxima_index], 'maxima': close[maxima_index]})

    extrema = pd.concat([minima, maxima], ignore_index=True, sort=True, axis=0)

    extrema = extrema.sort_values(by=['date'])
    extrema.reset_index(drop=True)

    return extrema


def _group_extrema(extrema):
    max_grouper = (~extrema['maxima'].isna()).cumsum()
    extrema['minima2'] = (extrema.groupby(max_grouper, group_keys=False)
                          .apply(lambda g: g['minima'].where(g['minima'] == g['minima'].min()))
                          )
    min_grouper = (~extrema['minima'].isna()).cumsum()
    extrema['maxima2'] = (extrema.groupby(min_grouper, group_keys=False)
                          .apply(lambda g: g['maxima'].where(g['maxima'] == g['maxima'].max()))
                          )

    extrema = extrema.sort_values(by=['date'])

    return extrema


def _clean_extrema(extrema):
    extrema = extrema.drop(columns=['maxima', 'minima'])
    extrema = extrema.dropna(thresh=2)

    return extrema


def _reorganize_extrema(extrema):
    extrema.minima2.fillna(extrema.maxima2, inplace=True)
    extrema.loc[extrema['maxima2'].notnull(), 'maxima2'] = 'maxima'
    extrema.maxima2.fillna("minima", inplace=True)
    extrema.rename(columns={'minima2': 'extrema', 'maxima2': 'type'}, inplace=True)
    extrema = extrema.reset_index(drop=True)

    return extrema

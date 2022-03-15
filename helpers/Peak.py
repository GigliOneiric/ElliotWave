import signal

import numpy as np
import pandas as pd
from scipy.signal import argrelextrema


def minmax(df, n):

    df['maxima'] = df.iloc[argrelextrema(df.Close.values, np.greater,
                                         order=n)[0]]['Close']

    df['minima'] = df.iloc[argrelextrema(df.Close.values, np.less,
                                         order=n)[0]]['Close']

    max_grouper = (~df['maxima'].isna()).cumsum()
    df['minima2'] = (df.groupby(max_grouper, group_keys=False)
                     .apply(lambda g: g['minima'].where(g['minima'] == g['minima'].min()))
                     )
    min_grouper = (~df['minima'].isna()).cumsum()
    df['maxima2'] = (df.groupby(min_grouper, group_keys=False)
                     .apply(lambda g: g['maxima'].where(g['maxima'] == g['maxima'].max()))
                     )

    return df

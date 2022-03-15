import matplotlib.pyplot as plt
import pandas as pd


def plot_linechart(df):
    plt.plot(df.index, df['close'])
    plt.show()


def plot_extrema(extrema):
    minima_maxima = pd.DataFrame({'date': extrema.date})

    minima_maxima['minima'] = extrema.apply(lambda g: g['extrema'] if g['type'] == 'minima' else None, axis=1)
    minima_maxima['maxima'] = extrema.apply(lambda g: g['extrema'] if g['type'] == 'maxima' else None, axis=1)

    plt.scatter(minima_maxima.date, minima_maxima.minima, c='y')
    plt.scatter(minima_maxima.date, minima_maxima.maxima, c='r')

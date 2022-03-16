import matplotlib.pyplot as plt
import pandas as pd

from model import Wave


def plot_linechart(df):
    plt.plot(df.index, df['close'])


def plot_extrema(extrema):
    minima_maxima = pd.DataFrame({'date': extrema.date})

    minima_maxima['minima'] = extrema.apply(lambda g: g['extrema'] if g['type'] == 'minima' else None, axis=1)
    minima_maxima['maxima'] = extrema.apply(lambda g: g['extrema'] if g['type'] == 'maxima' else None, axis=1)

    plt.scatter(minima_maxima.date, minima_maxima.minima, c='y')
    plt.scatter(minima_maxima.date, minima_maxima.maxima, c='r')


def plot_wave(df: Wave):
    wave_start = pd.DataFrame({'date': df.wave_start_index, 'point': df.wave_start_point}, index=[0])
    wave_end = pd.DataFrame({'date': df.wave_end_index, 'point': df.wave_end_point}, index=[0])
    wave = pd.concat([wave_start, wave_end], ignore_index=True, axis=0)

    plt.plot(wave.date, wave.point, c='r')
    plt.annotate(df.wave_counter, (wave_end.date, wave_end.point))


def plot_show():
    plt.show()

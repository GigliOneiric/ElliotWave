import matplotlib.pyplot as plt
import pandas as pd

import config.Text
from model.WaveFinder import Wave


def plot_linechart(df):
    plt.plot(df.index, df[config.Text.close])


def plot_extrema(extrema):
    minima_maxima = pd.DataFrame({config.Text.date: extrema.date})

    minima_maxima[config.Text.minima] = extrema.apply(lambda g: g[config.Text.extrema] if g[config.Text.type] == config.Text.minima else None, axis=1)
    minima_maxima[config.Text.maxima] = extrema.apply(lambda g: g[config.Text.extrema] if g[config.Text.type] == config.Text.maxima else None, axis=1)

    plt.scatter(minima_maxima.date, minima_maxima.minima, c='y')
    plt.scatter(minima_maxima.date, minima_maxima.maxima, c='r')


def plot_wave(df: Wave):
    wave_start = pd.DataFrame({config.Text.date: df.wave_start_index, config.Text.point: df.wave_start_point}, index=[0])
    wave_end = pd.DataFrame({config.Text.date: df.wave_end_index, config.Text.point: df.wave_end_point}, index=[0])
    wave = pd.concat([wave_start, wave_end], ignore_index=True, axis=0)

    plt.plot(wave.date, wave.point, c='r')
    plt.annotate(df.wave_counter, (wave_end.date, wave_end.point))


def plot_waves(wave_list):
    number_of_elements = len(wave_list)

    for i in range(number_of_elements):
        wave = wave_list[i]
        plot_wave(wave)


def plot_show():
    plt.show()

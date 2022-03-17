from helpers.Trend import trend_mannkendall
from model.Wave import Wave


class WavePattern(object):

    def __init__(self):
        self._wave = None
        self._wave_list = []

    @property
    def wave_list(self):
        return self._wave_list

    @wave_list.setter
    def wave_list(self, wave_list):
        self._wave_list = wave_list

    def add_wave(self, wave):
        self._wave_list.append(wave)

    def add_waves(self, minima_maxima):
        minima_maxima_counter = len(minima_maxima.index)

        start = self.find_good_start(minima_maxima, 0)

        for i in range(start, minima_maxima_counter-1):
            wave = Wave(minima_maxima['date'][i], minima_maxima['date'][i+1], minima_maxima['extrema'][i],
                        minima_maxima['extrema'][i+1])

            wave.wave_counter = start
            start = start + 1

            self.add_wave(wave)

    @staticmethod
    def find_good_start(minima_maxima, start):
        _start = start
        trend = trend_mannkendall(minima_maxima)

        if trend == 'increasing' and minima_maxima['type'][start] == 'maxima':
            _start = 1
        elif trend == 'decreasing' and minima_maxima['type'][start] == 'minima':
            _start = 1

        return _start

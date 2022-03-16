from model.Wave import Wave


class WavePattern(object):

    def __init__(self):
        self.wave = None
        self.wave_list = []

    @property
    def wave_list(self):
        return self._wave_list

    @wave_list.setter
    def wave_list(self, wave_list):
        self._wave_list = wave_list

    def add_wave(self, _wave):
        self._wave_list.append(_wave)

    def add_waves(self, minima_maxima):
        wave = Wave(minima_maxima['date'][1], minima_maxima['date'][2], minima_maxima['extrema'][1],
                    minima_maxima['extrema'][2])

        self.add_wave(wave)

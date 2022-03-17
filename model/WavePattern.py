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

        for i in range(1, minima_maxima_counter-1):
            wave = Wave(minima_maxima['date'][i], minima_maxima['date'][i+1], minima_maxima['extrema'][i],
                        minima_maxima['extrema'][i+1])

            wave.wave_counter = i

            self.add_wave(wave)

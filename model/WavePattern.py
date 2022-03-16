import wave
from typing import List, Any

from model.Wave import Wave

class WavePattern(object):

    def __init__(self):
        self.wave_list = []

    @property
    def wave_list(self):
        return self.wave_list()

    @wave_list.setter
    def add_wave(self, _wave):
        self.wave_list.append(_wave)

    @wave_list.setter
    def delete_wave(self, index):
        self.wave_list.pop(index)

    @wave_list.setter
    def add_waves(self, minima_maxima):
        minima_maxima_counter = len(minima_maxima.index)
        print(minima_maxima_counter)



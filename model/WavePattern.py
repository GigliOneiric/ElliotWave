class WavePattern(object):
    def __init__(self):
        self.wave_list = []

    @property
    def wave_list(self):
        return self.wave_list()

    @wave_list.setter
    def add_wave(self, wave):
        self.wave_list.append(wave)

    @wave_list.setter
    def delete_wave(self, index):
        self.wave_list.pop(index)




class WavePattern(object):

    def __init__(self, wave_list, name):
        self._name = name
        self._wave_list = wave_list

    @property
    def name(self):
        return self._name

    @name.setter
    def wave_list(self, name):
        self._name = name

    @property
    def wave_list(self):
        return self._wave_list

    @name.setter
    def name(self, wave_list):
        self._wave_list = wave_list

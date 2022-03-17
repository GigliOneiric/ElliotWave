class Wave(object):

    def __init__(self, wave_start_index, wave_end_index, wave_start_point, wave_end_point):
        self._wave_start_index = wave_start_index
        self._wave_end_index = wave_end_index
        self._wave_start_point = wave_start_point
        self._wave_end_point = wave_end_point

        self._wave_counter = int

    @property
    def wave_start_index(self):
        return self._wave_start_index

    @wave_start_index.setter
    def wave_start_index(self, wave_start_index):
        self._wave_start_index = wave_start_index

    @property
    def wave_end_index(self):
        return self._wave_end_index

    @wave_end_index.setter
    def wave_end_index(self, wave_end_index):
        self._wave_end_index = wave_end_index

    @property
    def wave_start_point(self):
        return self._wave_start_point

    @wave_start_point.setter
    def wave_start_point(self, wave_start_point):
        self._wave_start_point = wave_start_point

    @property
    def wave_end_point(self):
        return self._wave_end_point

    @wave_end_point.setter
    def wave_end_point(self, wave_end_point):
        self._wave_end_point = wave_end_point

    @property
    def wave_counter(self):
        return self._wave_counter

    @wave_counter.setter
    def wave_counter(self, wave_counter):
        self._wave_counter = wave_counter

    @property
    def wave_length(self):
        return abs(self.wave_start_point - self.wave_end_point)



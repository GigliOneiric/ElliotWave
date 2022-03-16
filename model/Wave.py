class Wave(object):

    def __init__(self, start_index, end_index, start_point, end_point):
        self.start_index = start_index
        self.end_index = end_index
        self.start_point = start_point
        self.end_point = end_point

        self.count = int

    @property
    def wave_start_index(self):
        return self.start_index

    @property
    def wave_end_index(self):
        return self.end_index

    @property
    def wave_start_point(self):
        return self.start_point

    @property
    def wave_end_point(self):
        return self.end_point

    @property
    def wave_length(self):
        return abs(self.start_point - self.end_point)

    @property
    def wave_count(self):
        return self.count

    @wave_count.setter
    def wave_count(self, value):
        self.count = value



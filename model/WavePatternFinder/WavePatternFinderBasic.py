import config.Text
from helpers.AnalyzerHighLow import AnalyzerHighLow

from helpers.IndexTools import last_index
from helpers.AnalyzerExtrema import minmax
from model.WaveFinder.WaveFinderBasic import WaveFinderBasic
from model.WavePatternFinder.WavePatternFinderCorrection import find_correction
from model.WavePatternFinder.WavePatternFinderImpulse import find_impulse


class WavePatternFinderBasic(object):

    def __init__(self, df, find_point_name, window_size):
        self._wave_list = []
        self._df = df
        self.find_point_name = find_point_name
        self._window_size = window_size

    def find_wave_pattern(self, idx_start):
        # Calculate Minima/Maxima
        significant_points = self.option_significant_points()

        # Build
        self._wave_list = WaveFinderBasic()
        self._wave_list.add_waves(significant_points, idx_start)
        self._wave_list = self._wave_list.wave_list

        impulse_pattern = find_impulse(self._wave_list, idx_start)

        idx_end = last_index(impulse_pattern)

        correction_pattern = find_correction(self._wave_list, idx_end + idx_start)

        return [impulse_pattern, correction_pattern]

    def option_significant_points(self):
        if self.find_point_name == config.Text.extrema:
            significant_points = minmax(self._df, self._window_size)
        elif self.find_point_name == config.Text.high_low:
            significant_points = AnalyzerHighLow(self._df).highlow()

        return significant_points





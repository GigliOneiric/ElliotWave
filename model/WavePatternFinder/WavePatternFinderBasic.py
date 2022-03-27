from helpers.IndexTools import last_index
from helpers.PeakAnalyzer import minmax
from model.WaveFinder.WaveFinderBasic import WaveFinderBasic
from model.WavePatternFinder.WavePatternFinderCorrection import find_correction
from model.WavePatternFinder.WavePatternFinderImpulse import find_impulse


class WavePatternFinderBasic(object):

    def __init__(self, df, window_size):
        self._wave_list = []
        self._df = df
        self._window_size = window_size

    def find_wave_pattern(self, idx_start):
        # Calculate Minima/Maxima
        minima_maxima = minmax(self._df, self._window_size)

        # Build
        self._wave_list = WaveFinderBasic()
        self._wave_list.add_waves(minima_maxima, idx_start)
        self._wave_list = self._wave_list.wave_list

        impulse_pattern = find_impulse(self._wave_list, idx_start)

        idx_end = last_index(impulse_pattern)

        correction_pattern = find_correction(self._wave_list, idx_end)

        return [impulse_pattern, correction_pattern]

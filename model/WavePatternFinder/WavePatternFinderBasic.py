import config.Text
from helpers.PeakAnalyzer import minmax
from model.WaveFinder.WaveFinderBasic import WaveFinderBasic
from model.WavePatternFinder.WavePattern import WavePattern
from model.WavePatternFinder.WavePatternFinderCorrection import find_correction_wave
from model.WavePatternFinder.WavePatternFinderImpulse import find_impulsive_wave


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

        impulse_wave_list = find_impulsive_wave(self._wave_list, idx_start)
        impulse_pattern = WavePattern(impulse_wave_list, config.Text.impulse)

        correction_wave_list = find_correction_wave(self._wave_list, idx_start + 5)
        correction_pattern = WavePattern(correction_wave_list, 'zigzag')

        return [impulse_pattern, correction_pattern]

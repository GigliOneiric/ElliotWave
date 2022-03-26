import config.Text
from helpers.PeakAnalyzer import minmax
from model.WaveFinder.WaveFinderBasic import WaveFinderBasic
from model.WavePatternFinder.WavePattern import WavePattern
from model.WavePatternFinder.WavePatternFinderCorrection import find_correction_wave
from model.WavePatternFinder.WavePatternFinderImpulse import find_impulsive_wave


class WavePatternFinder(object):

    def __init__(self, df):
        self._wave_list = []
        self._df = df

    def find_wave_pattern(self, idx_start):
        # Calculate Minima/Maxima
        minima_maxima = minmax(self._df, 2)

        # Build
        self._wave_list = WaveFinderBasic()
        self._wave_list.add_waves(minima_maxima, idx_start)
        self._wave_list = self._wave_list.wave_list

        impulse_wave_list = find_impulsive_wave(self._wave_list, idx_start)
        correction_wave_list = find_correction_wave(self._wave_list, idx_start+5)

        self._wave_list = impulse_wave_list + correction_wave_list

        return self._wave_list

    def find_wave_pattern2(self, idx_start):
        # Calculate Minima/Maxima
        minima_maxima = minmax(self._df, 1)

        # Build
        self._wave_list = WaveFinderBasic()
        self._wave_list.add_waves(minima_maxima, idx_start)
        self._wave_list = self._wave_list.wave_list

        impulse_wave_list = find_impulsive_wave(self._wave_list, idx_start)
        impulse_pattern = WavePattern(impulse_wave_list, config.Text.impulse)

        correction_wave_list = find_correction_wave(self._wave_list, idx_start + 5)
        correction_pattern = WavePattern(correction_wave_list, 'zigzag')

        return [impulse_pattern, correction_pattern]

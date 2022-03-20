from model.WaveFinder.WaveFinderBasic import WaveFinderBasic
from helpers.PeakAnalyzer import minmax


def find_impulsive_wave(df, idx_start):
    # Calculate Minima/Maxima
    minima_maxima = minmax(df, 2)

    # Build
    wave_list = WaveFinderBasic()
    wave_list.add_waves(minima_maxima)
    wave_list = wave_list.wave_list

    wave1 = wave_list[idx_start + 0]
    wave2 = wave_list[idx_start + 1]
    wave3 = wave_list[idx_start + 2]
    wave4 = wave_list[idx_start + 3]
    wave5 = wave_list[idx_start + 4]

    return [wave1, wave2, wave3, wave4, wave5]

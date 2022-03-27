import config.Text
from model.WavePatternFinder.WavePattern import WavePattern


def find_correction(df, idx_start):
    name = config.Text.zigzag
    waves = find_zigzag(df, idx_start)

    correction = WavePattern(waves, name)

    return correction


def find_zigzag(wave_list, idx_start):
    waveA = wave_list[idx_start + 0]
    waveA.wave_counter = config.Text.a

    waveB = wave_list[idx_start + 1]
    waveB.wave_counter = config.Text.b

    waveC = wave_list[idx_start + 2]
    waveC.wave_counter = config.Text.c

    return [waveA, waveB, waveC]

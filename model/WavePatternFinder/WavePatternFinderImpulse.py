import config.Text
from model.WavePatternFinder.WavePattern import WavePattern


def find_impulse(df, idx_start):
    name = config.Text.impulse
    waves = find_impulsive_wave(df, idx_start)

    impulse = WavePattern(waves, name)

    return impulse


def find_impulsive_wave(wave_list, idx_start):

    wave1 = wave_list[idx_start + 0]
    wave1.wave_counter = 1

    wave2 = wave_list[idx_start + 1]
    wave2.wave_counter = 2

    wave3 = wave_list[idx_start + 2]
    wave3.wave_counter = 3

    wave4 = wave_list[idx_start + 3]
    wave4.wave_counter = 4

    wave5 = wave_list[idx_start + 4]
    wave5.wave_counter = 5

    return [wave1, wave2, wave3, wave4, wave5]

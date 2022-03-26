def find_correction_wave(df, idx_start):
    waves = find_zigzag(df, idx_start)

    return waves


def find_zigzag(wave_list, idx_start):
    waveA = wave_list[idx_start + 0]
    waveA.wave_counter = 'A'

    waveB = wave_list[idx_start + 1]
    waveB.wave_counter = 'B'

    waveC = wave_list[idx_start + 2]
    waveC.wave_counter = 'C'

    return [waveA, waveB, waveC]

import config.Text


class Impulse:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def conditions(self):
        conditions = {
            'w2_1': {
                config.Text.waves: ['wave1', 'wave2'],
                config.Text.function: lambda wave1, wave2: wave1.wave_length > wave2.wave_length,
                config.Text.message: 'Wave 1 is longer than wave 2'

            },
            'w3_2': {
                config.Text.waves: ['wave2', 'wave3'],
                config.Text.function: lambda wave2, wave3: wave2.wave_length < wave3.wave_length,
                config.Text.message: 'Wave 3 is longer than wave 2'
            },
            'w3': {
                config.Text.waves: ['wave1', 'wave2', 'wave3', 'wave4'],
                config.Text.function: lambda wave1, wave2, wave3, wave4: wave3.wave_length > wave1.wave_length
                                                                         and wave3.wave_length > wave2.wave_length
                                                                         and wave3.wave_length > wave4.wave_length,
                config.Text.message: 'Wave 3 is the shortest'
            },
            'w4_3': {
                config.Text.waves: ['wave3', 'wave4'],
                config.Text.function: lambda wave3, wave4: wave3.wave_length > wave4.wave_length,
                config.Text.message: 'Wave 3 is longer than wave 4'

            }
        }

        return conditions

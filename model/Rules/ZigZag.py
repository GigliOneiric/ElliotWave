import config.Text

class ZigZag:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def conditions(self):
        conditions = {
            'wa_b': {
                config.Text.waves: ['waveA', 'waveB'],
                config.Text.function: lambda waveA, waveB: waveA.wave_length > waveB.wave_length,
                config.Text.message: 'Wave A is shorter than wave B'

            },
            'wb_c': {
                config.Text.waves: ['waveB', 'waveC'],
                config.Text.function: lambda waveB, waveC: waveB.wave_length < waveC.wave_length,
                config.Text.message: 'Wave C is shorter than wave B'
            }
        }

        return conditions

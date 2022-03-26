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
                'waves': ['waveA', 'waveB'],
                'function': lambda waveA, waveB: waveA.wave_length < waveB.wave_length,
                'message': 'Wave A is shorter than wave B'

            },
            'wb_c': {
                'waves': ['waveB', 'waveC'],
                'function': lambda waveB, waveC: waveB.wave_length > waveC.wave_length,
                'message': 'Wave C is shorter than wave B'
            }
        }

        return conditions

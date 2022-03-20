class Impulse:
    def __init__(self, name: str):
        self.name = name
        self.conditions = self.conditions()

    def conditions(self):
        self.conditions = {
            "w2_1": {
                "waves": ["wave1", "wave2"],
                "function": lambda wave1, wave2: wave1.wave_length > wave2.wave_length,
                "message": "Wave 1 is longer than wave 2"

            },
            "w3_2": {
                "waves": ["wave2", "wave3"],
                "function": lambda wave2, wave3: wave3.wave_length > wave2.wave_length,
                "message": "Wave 3 is longer than wave 2"
            }
            ,
            "w4_3": {
                "waves": ["wave3", "wave4"],
                "function": lambda wave3, wave4: wave3.wave_length > wave4.wave_length,
                "message": "Wave 3 is longer than wave 4"

            }
        }

        return self.conditions

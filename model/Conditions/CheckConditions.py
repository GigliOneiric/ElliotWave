from model.Conditions.Impulse import Impulse
from model.Wave import Wave


class CheckConditions:

    def __init__(self, waves: list):
        self.waves = waves

    def check_rule(self, wavecondition):
        for rule, conditions in wavecondition.conditions.items():
            function = conditions.get('function')
            message = conditions.get('message')
            print(message)


            return True

class Check:

    def __init__(self, waves: list, logging):
        self._valid_rules = True
        self._waves = waves
        self._logging = logging

        _waves_dict = dict()
        for i, wave in enumerate(self._waves):
            # NYF if len waves = 3 -> map 1 - a etc
            key = f'wave{i + 1}'
            _waves_dict.setdefault(key, wave)

        self.waves = _waves_dict

    def check_rule(self, wave_condition):

        for key, value in wave_condition.conditions.items():
            number_of_waves = len(value['waves'])
            function = value['function']
            message = value['message']

            if number_of_waves == 2:
                self._check_rule_two_waves(key, value, function, message)
            if number_of_waves == 3:
                self._check_rule_three_waves(key, value, function, message)
            if number_of_waves == 3:
                self._check_rule_four_waves(key, value, function, message)

        return self._valid_rules

    def _check_rule_two_waves(self, key, value, function, message):
        # Get the first waves from rules [can be wave1, wave2, wave3, wave4]
        wave1 = self.waves[value.get('waves')[0]]
        wave2 = self.waves[value.get('waves')[1]]

        if not function(wave1, wave2):
            if self._logging is True:
                print(f'Rule Violation of {key} for condition {value}: {message}')
            self._valid_rules = False

    def _check_rule_three_waves(self, key, value, function, message):
        # Get the first waves from rules [can be wave1, wave2, wave3, wave4]
        wave1 = self.waves[value.get('waves')[0]]
        wave2 = self.waves[value.get('waves')[1]]
        wave3 = self.waves[value.get('waves')[2]]

        if not function(wave1, wave2, wave3):
            if self._logging is True:
                print(f'Rule Violation of {key} for condition {value}: {message}')
            self._valid_rules = False

    def _check_rule_four_waves(self, key, value, function, message):
        # Get the first waves from rules [can be wave1, wave2, wave3, wave4]
        wave1 = self.waves[value.get('waves')[0]]
        wave2 = self.waves[value.get('waves')[1]]
        wave3 = self.waves[value.get('waves')[2]]
        wave4 = self.waves[value.get('waves')[3]]

        if not function(wave1, wave2, wave3, wave4):
            if self._logging is True:
                print(f'Rule Violation of {key} for condition {value}: {message}')
            self._valid_rules = False


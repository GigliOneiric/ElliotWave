import config.Text


class Check:

    def __init__(self, wave_pattern: list, rule, logging):
        self._waves = None
        self._rule = rule
        self._valid_rules = True
        self._wave_pattern = wave_pattern
        self._logging = logging

        self.map_waves()

    def map_waves(self):
        _waves_dict = dict()

        for e, wave_pattern in enumerate(self._wave_pattern):
            for i, wave in enumerate(wave_pattern.wave_list):
                if wave_pattern.name == config.Text.impulse and self._rule == config.Text.impulse:
                    key = f'wave{i + 1}'
                    _waves_dict.setdefault(key, wave)
                elif wave_pattern.name == config.Text.zigzag and self._rule == config.Text.zigzag:
                    key = f'wave{chr(i + 65)}'
                    _waves_dict.setdefault(key, wave)

            self._waves = _waves_dict

    def check_rule(self, wave_condition):

        for key, value in wave_condition.conditions.items():
            number_of_waves = len(value[config.Text.waves])
            function = value[config.Text.function]
            message = value[config.Text.message]

            if number_of_waves == 2:
                self._check_rule_two_waves(key, value, function, message)
            if number_of_waves == 3:
                self._check_rule_three_waves(key, value, function, message)
            if number_of_waves == 3:
                self._check_rule_four_waves(key, value, function, message)

        return self._valid_rules

    def _check_rule_two_waves(self, key, value, function, message):
        # Get the first waves from rules [can be wave1, wave2, wave3, wave4]
        wave1 = self._waves[value.get(config.Text.waves)[0]]
        wave2 = self._waves[value.get(config.Text.waves)[1]]

        if not function(wave1, wave2):
            if self._logging is True:
                print(f'Rule Violation of {key} for condition {value}: {message}')
            self._valid_rules = False

    def _check_rule_three_waves(self, key, value, function, message):
        # Get the first waves from rules [can be wave1, wave2, wave3, wave4]
        wave1 = self._waves[value.get(config.Text.waves)[0]]
        wave2 = self._waves[value.get(config.Text.waves)[1]]
        wave3 = self._waves[value.get(config.Text.waves)[2]]

        if not function(wave1, wave2, wave3):
            if self._logging is True:
                print(f'Rule Violation of {key} for condition {value}: {message}')
            self._valid_rules = False

    def _check_rule_four_waves(self, key, value, function, message):
        # Get the first waves from rules [can be wave1, wave2, wave3, wave4]
        wave1 = self._waves[value.get(config.Text.waves)[0]]
        wave2 = self._waves[value.get(config.Text.waves)[1]]
        wave3 = self._waves[value.get(config.Text.waves)[2]]
        wave4 = self._waves[value.get(config.Text.waves)[3]]

        if not function(wave1, wave2, wave3, wave4):
            if self._logging is True:
                print(f'Rule Violation of {key} for condition {value}: {message}')
            self._valid_rules = False


import pandas as pd

import config.Text


class AnalyzerHighLow(object):

    def __init__(self, df):
        self.df = df.close.values
        self.highs = pd.DataFrame(columns=[config.Text.date, config.Text.extrema, config.Text.type])
        self.lows = pd.DataFrame(columns=[config.Text.date, config.Text.extrema, config.Text.type])
        self.high_low = pd.DataFrame(columns=[config.Text.date, config.Text.extrema, config.Text.type])

    def highlow(self):
        idx_start = 0

        self.find_high(self.df, idx_start)
        self.find_low(self.df, idx_start)

        self.high_low = pd.concat([self.highs, self.lows], ignore_index=True, sort=True, axis=0)
        self.high_low = self.high_low.sort_values(by=[config.Text.date])
        self.high_low = self.high_low.reset_index(drop=True)

        return self.high_low

    def find_high(self, high_low, idx_start):
        pvt_high = high_low[idx_start]
        reached = False

        for i in range(idx_start + 1, len(high_low)):
            act_high = high_low[i]

            if act_high > pvt_high:
                reached = True
                pvt_high = act_high

            elif act_high < pvt_high and reached is True:
                self.highs.loc[i] = [i, pvt_high, config.Text.maxima]
                return self.find_high(high_low, i)

            elif act_high < pvt_high:
                pvt_high = high_low[i]

            if (reached is True) and (i == (len(high_low) - 1)):
                self.highs.loc[i] = [i, pvt_high, config.Text.maxima]

    def find_low(self, high_low, idx_start):
        pvt_low = high_low[idx_start]
        reached = False

        for i in range(idx_start + 1, len(high_low)):
            act_low = high_low[i]

            if act_low < pvt_low:
                reached = True
                pvt_low = act_low

            elif act_low > pvt_low and reached is True:
                self.lows.loc[i] = [i, pvt_low, config.Text.minima]
                return self.find_low(high_low, i)

            elif act_low > pvt_low:
                pvt_low = high_low[i]

            if (reached is True) and (i == (len(high_low) - 1)):
                self.lows.loc[i] = [i, pvt_low, config.Text.minima]

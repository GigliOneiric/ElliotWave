import pandas as pd

import config.Text


def read_csv():
    col_names = [config.Text.date, config.Text.open, config.Text.high, config.Text.low, config.Text.close, config.Text.volume]
    data = pd.read_csv(r'C:\Users\Tobias\PycharmProjects\ElliotWave\data\btc-usd_1d.csv', names=col_names, skiprows=1)

    df = pd.DataFrame(data)

    return df

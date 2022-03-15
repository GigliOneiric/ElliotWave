import pandas as pd


def read_csv():
    col_names = ["date", "open", "high", "low", "close", "volume"]
    data = pd.read_csv(r'data\btc-usd_1d.csv', names=col_names, skiprows=1)

    df = pd.DataFrame(data)

    return df

import pandas as pd


def readCSV():
    data = pd.read_csv(r'data\btc-usd_1d.csv')
    df = pd.DataFrame(data, columns=["Date", "Open", "High", "Low", "Close"])

    return df

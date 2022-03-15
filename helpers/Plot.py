import matplotlib.pyplot as plt


def plot(df):
    plt.scatter(df.index, df.maxima, c='r')
    plt.scatter(df.index, df.minima, c='g')
    plt.scatter(df.index, df.minima2, c='y')
    plt.scatter(df.index, df.maxima2, c='b')

    plt.plot(df.index, df['Close'])

    plt.show()

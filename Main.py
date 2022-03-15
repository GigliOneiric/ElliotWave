from helpers.Peak import minmax
from helpers.FileReader import read_csv
from helpers.Plot import *

# Read CSV
df = read_csv()

# Calculate Minima/Maxima
minima_maxima = minmax(df, 1)

# Plot results
plot_extrema(minima_maxima)
plot_linechart(df)



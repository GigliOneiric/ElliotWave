from helpers.Peak import minmax
from helpers.FileReader import read_csv
from helpers.Plot import *
from model.WavePattern import *

# Read CSV
df = read_csv()

# Calculate Minima/Maxima
minima_maxima = minmax(df, 1)

# Build
waves = WavePattern()
waves.add_waves(minima_maxima)


# Plot results
plot_linechart(df)
plot_extrema(minima_maxima)
plot_waves(waves.wave_list)
plot_show()

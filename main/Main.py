from helpers.Peak import minmax
from helpers.FileReader import read_csv
from helpers.Plot import *
from model.WavePattern import *

# Read CSV
df = read_csv()

# Calculate Minima/Maxima
minima_maxima = minmax(df, 1)

# Build
wave = WavePattern()
wave.add_waves(minima_maxima)

wave_1 = Wave(minima_maxima['date'][1], minima_maxima['date'][2], minima_maxima['extrema'][1], minima_maxima['extrema'][2])
wave_1.wave_count = '1'

# Plot results
plot_linechart(df)
plot_extrema(minima_maxima)
plot_wave(wave_1)
plot_show()

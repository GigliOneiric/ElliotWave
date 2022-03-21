from helpers.FileReader import read_csv
from helpers.PeakAnalyzer import minmax
from helpers.Plot import *
from model.Rules.Check import Check
from model.Rules.Impulse import *
# Read CSV
from model.WaveFinder.WaveFinderImpulse import find_impulsive_wave

df = read_csv()

# Calculate Minima/Maxima
minima_maxima = minmax(df, 2)

# Build
waves = find_impulsive_wave(df, 0)

impulse = Impulse('impulse')
rules_to_check = [impulse]

for rule in rules_to_check:
    Check(waves, logging=True).check_rule(rule)

# Plot results
plot_linechart(df)
plot_extrema(minima_maxima)
plot_waves(waves)
plot_show()

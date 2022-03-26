from helpers.FileReader import read_csv
from helpers.Plot import *
from model.Rules.Check import *
from model.Rules.Impulse import *
from model.Rules.ZigZag import *
from model.WavePatternFinder.WavePatternFinder import *
# Read CSV

df = read_csv()

# Calculate Minima/Maxima
minima_maxima = minmax(df, 2)

# Build
wave_pattern = WavePatternFinder(df, window_size=2).find_wave_pattern(idx_start=0)

impulse = Impulse(config.Text.impulse)
zigzag = ZigZag(config.Text.zigzag)
rules_to_check = [impulse, zigzag]

for rule in rules_to_check:
    Check(wave_pattern, rule.name, logging=True).check_rule(rule)

# Plot results
plot_linechart(df)
plot_extrema(minima_maxima)
plot_pattern(wave_pattern)
plot_show()

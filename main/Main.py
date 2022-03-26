from helpers.FileReader import read_csv
from helpers.PeakAnalyzer import minmax
from helpers.Plot import *
from model.Rules.Check import Check
from model.Rules.Impulse import *
from model.Rules.ZigZag import ZigZag
from model.WavePatternFinder.WavePatternFinder import WavePatternFinder
# Read CSV

df = read_csv()

# Calculate Minima/Maxima
minima_maxima = minmax(df, 2)

# Build
wave_pattern = WavePatternFinder(df).find_wave_pattern2(1)
waves = WavePatternFinder(df).find_wave_pattern(1)

impulse = Impulse(config.Text.impulse)
zigzag = ZigZag(config.Text.zigzag)
rules_to_check = [impulse, zigzag]

for rule in rules_to_check:
    Check(wave_pattern, rule.name, logging=True).check_rule(rule)

# Plot results
plot_linechart(df)
plot_extrema(minima_maxima)
plot_waves(waves)
plot_show()

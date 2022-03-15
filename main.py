from helpers.Peak import minmax
from helpers.FileReader import readCSV
from helpers.Plot import plot

# Read CSV
df = readCSV()

# Calculate Minima/Maxima
df = minmax(df, 1)

# Plot results
plot(df)



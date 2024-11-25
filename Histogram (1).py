import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
file_path = "smartwatch.csv"
df = pd.read_csv(file_path)

# Plot histograms for all numeric columns
df.hist(figsize=(12, 12), bins=30, edgecolor='black')

# Set overall title for the histograms
plt.suptitle('Histograms of Numeric Columns', fontsize=12)

# Display the plot
plt.show()

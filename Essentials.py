 import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
file_path = "Fact_smartwatch.csv"
df = pd.read_csv(file_path)

# Find the data types of each column
data_types = df.dtypes
print("Data Types:\n", data_types)

# Find the number of unique values in each column
unique_values = df.nunique()
print("\nUnique Values:\n", unique_values)

# Find the number of missing values in each column
missing_values = df.isnull().sum()
print("\nMissing Values:\n", missing_values)

# Sum up missing values in each column
missing_values_count = df.isnull().sum()



# Create a heatmap to visualize missing values
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis', annot=True)

# Show the plot
plt.show()


# Print the sum of missing values for each column
print("Sum of missing values in each column:\n", missing_values_count)


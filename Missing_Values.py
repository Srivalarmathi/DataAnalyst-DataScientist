import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno

# Load the CSV file into a DataFrame
file_path =  "smartwatch.csv"
df = pd.read_csv(file_path)

# Calculate the count of missing values for each column
missing_values_count = df.isnull().sum()

# Display the count of missing values
print("Missing Values Count:\n", missing_values_count)

# Create a heatmap to visualize missing values
plt.figure(figsize=(12, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis', yticklabels=False)
plt.title('Heatmap of Missing Values')
plt.show()

# Generate a missing values matrix
msno.matrix(df, figsize=(12, 6))
plt.title('Missing Values Matrix')
plt.show()

# Create a dendrogram to visualize the hierarchical clustering of missing value patterns
msno.dendrogram(df)
plt.title('Dendrogram of Missing Values')
plt.show()

# Optionally, save the count of missing values to a CSV file
missing_values_count.to_csv( "missing_value_matrix_output.csv", header=["Missing Values"])

print("Missing values analysis completed and visualized successfully.")

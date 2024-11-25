import pandas as pd

# Load the CSV file into a DataFrame
file_path = "smartwatch.csv"
df = pd.read_csv(file_path)


# Function to calculate and display quantile statistics for all columns
def calculate_quantile_statistics(df):
    statistics = {}

    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            min_value = df[column].min()
            q1 = df[column].quantile(0.25)
            median = df[column].median()
            q3 = df[column].quantile(0.75)
            max_value = df[column].max()
            range_value = max_value - min_value
            iqr = q3 - q1

            statistics[column] = {
                'Minimum Value': min_value,
                'Q1 (25th percentile)': q1,
                'Median (50th percentile)': median,
                'Q3 (75th percentile)': q3,
                'Maximum Value': max_value,
                'Range': range_value,
                'Inter-quantile Range (IQR)': iqr
            }

    return statistics


# Calculate and display the quantile statistics for all numeric columns
quantile_statistics = calculate_quantile_statistics(df)
for column, stats in quantile_statistics.items():
    print(f"\nColumn: {column}")
    for stat_name, value in stats.items():
        print(f"{stat_name}: {value}")

# Optionally, you can save the statistics to a file
output_path = "QuantileOutput.csv"
pd.DataFrame(quantile_statistics).T.to_csv(output_path)

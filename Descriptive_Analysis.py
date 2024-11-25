import pandas as pd
import numpy as np
from scipy.stats import kurtosis, skew

# Load the CSV file into a DataFrame
file_path = "smartwatch.csv"
df = pd.read_csv(file_path)


# Function to calculate Median Absolute Deviation
def median_absolute_deviation(series):
    median = series.median()
    return np.median(np.abs(series - median))


# Function to calculate descriptive statistics
def calculate_descriptive_statistics(df):
    statistics = {}

    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            mean_value = df[column].mean()
            mode_value = df[column].mode().iloc[0] if not df[column].mode().empty else np.nan
            std_dev = df[column].std()
            sum_value = df[column].sum()
            mad = median_absolute_deviation(df[column])
            coeff_var = std_dev / mean_value if mean_value != 0 else np.nan
            kurtosis_value = kurtosis(df[column].dropna(), nan_policy='omit')
            skewness_value = skew(df[column].dropna(), nan_policy='omit')

            statistics[column] = {
                'Mean': mean_value,
                'Mode': mode_value,
                'Standard Deviation': std_dev,
                'Sum': sum_value,
                'Median Absolute Deviation': mad,
                'Coefficient of Variation': coeff_var,
                'Kurtosis': kurtosis_value,
                'Skewness': skewness_value
            }

    return statistics


# Calculate and display the descriptive statistics for all numeric columns
descriptive_statistics = calculate_descriptive_statistics(df)
for column, stats in descriptive_statistics.items():
    print(f"\nColumn: {column}")
    for stat_name, value in stats.items():
        print(f"{stat_name}: {value}")

# Optionally, you can save the statistics to a file
output_path = "descriptive_analysis_output.csv"
pd.DataFrame(descriptive_statistics).T.to_csv(output_path)

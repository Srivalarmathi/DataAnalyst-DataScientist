import pandas as pd

# Load the CSV file into a DataFrame
file_path = "smartwatch.csv"
df = pd.read_csv(file_path)

# Select only numeric columns
numeric_df = df.select_dtypes(include='number')

# Calculate correlation matrices
pearson_corr = numeric_df.corr(method='pearson')
spearman_corr = numeric_df.corr(method='spearman')
kendall_corr = numeric_df.corr(method='kendall')

# Function to highlight highly correlated variables
def highlight_highly_correlated(corr_matrix, threshold=0.8):
    return corr_matrix.map(lambda x: 'background-color: yellow' if abs(x) >= threshold else '', na_action='ignore')

# Apply highlighting to correlation matrices
highlighted_pearson = pearson_corr.style.apply(highlight_highly_correlated, axis=None)
highlighted_spearman = spearman_corr.style.apply(highlight_highly_correlated, axis=None)
highlighted_kendall = kendall_corr.style.apply(highlight_highly_correlated, axis=None)

# Save correlation matrices to CSV files
pearson_corr.to_csv("pearson_correlation.csv")
spearman_corr.to_csv("spearman_correlation.csv")
kendall_corr.to_csv("kendall_correlation.csv")

# Save highlighted correlation matrices to HTML files (CSV files do not support styling)
highlighted_pearson.to_html("highlighted_pearson_correlation.html")
highlighted_spearman.to_html("highlighted_spearman_correlation.html")
highlighted_kendall.to_html("highlighted_kendall_correlation.html")

print("Correlation matrices and highlighted versions saved successfully.")

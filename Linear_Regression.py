import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, mean_absolute_percentage_error

# Load the cleaned data
df = pd.read_csv("smartwatch.csv")

# Define the features and target variable
features = ['age', 'gender', 'height', 'weight', 'steps', 'calories', 'distance',
            'entropy_heart', 'entropy_setps', 'resting_heart', 'corr_heart_steps',
            'norm_heart', 'intensity_karvonen', 'sd_norm_heart', 'steps_times_distance']
target = 'hear_rate'

X = df[features]
y = df[target]

# Split the dataset (80% for training and 20% for testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mape = mean_absolute_percentage_error(y_test, y_pred)

print(f'Mean Absolute Error: {mae}')
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')
print(f'Mean Absolute Percentage Error: {mape}')

# Identify key points to annotate (e.g., top 10 largest errors)
errors = np.abs(y_test - y_pred)
top_errors_indices = errors.argsort()[-10:]  # Get the indices of the top 10 largest errors

# Visualize the results
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue', label='Predictions')
plt.xlabel('Actual Calories')
plt.ylabel('Predicted Calories')
plt.title('Actual vs. Predicted Calories')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--', label='Ideal Line')

# Plot the linear regression line
plt.plot(np.unique(y_test), np.poly1d(np.polyfit(y_test, y_pred, 1))(np.unique(y_test)), color='green', label='Regression Line')

# Annotate the key points
for i in top_errors_indices:
    plt.text(y_test.iloc[i], y_pred[i], f'({y_test.iloc[i]}, {y_pred[i]:.2f})', fontsize=9, ha='right')

plt.legend()
plt.grid(True)
plt.show()

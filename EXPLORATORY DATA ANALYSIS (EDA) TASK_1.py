# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
tips = sns.load_dataset('tips')

# Step 2: Understand the data
print(tips.head())
print(tips.info())
print(tips.describe())

# Step 3: Descriptive statistics
print(tips.describe())

# Step 4: Data visualization
# Histogram for the distribution of total_bill
plt.figure(figsize=(8, 6))
sns.histplot(tips['total_bill'], bins=20, kde=True)
plt.title('Distribution of Total Bill')
plt.show()

# Scatter plot to visualize the relationship between total_bill and tip
plt.figure(figsize=(8, 6))
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time')
plt.title('Scatter Plot of Total Bill vs Tip')
plt.show()

# Heatmap to visualize correlations between numerical features
plt.figure(figsize=(10, 8))
correlation_matrix = tips.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Heatmap of Correlation Matrix')
plt.show()

# Step 5: Identify correlations and outliers
print(tips.corr())

# Boxplot to identify outliers in total_bill
plt.figure(figsize=(8, 6))
sns.boxplot(x=tips['total_bill'])
plt.title('Boxplot of Total Bill')
plt.show()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("dataset/student-mat.csv", sep=";")

print("=" * 50)
print("STUDENT PERFORMANCE - EXPLORATORY DATA ANALYSIS")
print("=" * 50)

# 1. First five records
print("\nFirst 5 Records:")
print(df.head())

# 2. Dataset dimensions
print("\nDataset Shape:")
print(df.shape)

# 3. Dataset information
print("\nDataset Information:")
df.info()

# 4. Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# 5. Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 6. Duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# 7. Final grade analysis
print("\nFinal Grade Analysis:")
print(df["G3"].describe())

# 8. Average final grade
print("\nAverage Final Grade:")
print(df["G3"].mean())

# 9. Correlation analysis
print("\nCorrelation with Final Grade:")
print(
    df.corr(numeric_only=True)["G3"]
    .sort_values(ascending=False)
)

print("\nEDA ANALYSIS COMPLETED!")

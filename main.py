import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset.csv")

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df = df.fillna(df.mean(numeric_only=True))

# Standardize text
df.columns = df.columns.str.strip()

# Save cleaned data
df.to_csv("output/cleaned_data.csv", index=False)

# Generate report
print(df.describe())

# Create chart
df['math score'].plot(kind='hist')

plt.title("Math Score Distribution")
plt.savefig("output/chart.png")

print("Project Completed Successfully")


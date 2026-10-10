import pandas as pd
import matplotlib.pyplot as plt

# Create a sample Beauty and Wellness dataset
data = {
    "Product": [
        "Face Cream", "Shampoo", "Face Wash",
        "Hair Oil", "Body Lotion", "Face Cream",
        "Shampoo", "Sunscreen", "Face Wash", "Hair Oil"
    ],
    "Category": [
        "Skincare", "Haircare", "Skincare",
        "Haircare", "Bodycare", "Skincare",
        "Haircare", "Skincare", "Skincare", "Haircare"
    ],
    "Price": [
        250, 180, 150, 220, 300, 250, 180, 400, None, 220
    ],
    "Rating": [
        4.5, 4.2, 4.0, 4.3, 4.6, 4.5, 4.2, 4.8, 4.1, None
    ]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing numerical values with column averages
df["Price"] = df["Price"].fillna(df["Price"].mean())
df["Rating"] = df["Rating"].fillna(df["Rating"].mean())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Category counts
print("\nProduct Categories:")
print(df["Category"].value_counts())

# Save cleaned data
df.to_csv("cleaned_beauty_data.csv", index=False)

# Create a bar chart
df["Category"].value_counts().plot(kind="bar")
plt.title("Products by Category")
plt.xlabel("Category")
plt.ylabel("Number of Products")
plt.tight_layout()
plt.savefig("category_chart.png")
plt.show()

print("\nData cleaning completed successfully!")

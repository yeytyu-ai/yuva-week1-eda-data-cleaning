import os
import pandas as pd
import matplotlib.pyplot as plt

# Create folders
os.makedirs("output", exist_ok=True)
os.makedirs("plots", exist_ok=True)

# Load dataset
df = pd.read_csv("data/product_info.csv")

print("Original Dataset:")
print(df.head())

print("\nDataset Shape:", df.shape)

# Check missing values
missing_values = df.isnull().sum()
missing_values.to_csv("output/missing_values.csv")

# Remove duplicate records
df = df.drop_duplicates()

# Convert numeric columns
for column in ["price_usd", "rating"]:
    if column in df.columns:
        df[column] = pd.to_numeric(
            df[column], errors="coerce"
        )

# Fill missing numeric values with median
for column in ["price_usd", "rating"]:
    if column in df.columns:
        median_value = df[column].median()
        if pd.notna(median_value):
            df[column] = df[column].fillna(median_value)

# Save cleaned dataset
df.to_csv("output/cleaned_beauty_data.csv", index=False)

# Generate summary statistics
df.describe(include="all").to_csv(
    "output/summary_statistics.csv"
)

# Category distribution
if "primary_category" in df.columns:
    df["primary_category"].value_counts().plot(kind="bar")
    plt.title("Beauty Product Category Distribution")
    plt.xlabel("Category")
    plt.ylabel("Number of Products")
    plt.tight_layout()
    plt.savefig("plots/category_distribution.png")
    plt.close()

# Price histogram
if "price_usd" in df.columns:
    df["price_usd"].dropna().hist(bins=10)
    plt.title("Beauty Product Price Distribution")
    plt.xlabel("Price (USD)")
    plt.ylabel("Number of Products")
    plt.tight_layout()
    plt.savefig("plots/price_histogram.png")
    plt.close()

# Price box plot
if "price_usd" in df.columns:
    plt.figure()
    plt.boxplot(df["price_usd"].dropna())
    plt.title("Beauty Product Price Box Plot")
    plt.ylabel("Price (USD)")
    plt.tight_layout()
    plt.savefig("plots/price_boxplot.png")
    plt.close()

# Price vs rating scatter plot
if "price_usd" in df.columns and "rating" in df.columns:
    valid = df[["price_usd", "rating"]].dropna()

    plt.figure()
    plt.scatter(valid["price_usd"], valid["rating"])
    plt.title("Price vs Rating")
    plt.xlabel("Price (USD)")
    plt.ylabel("Rating")
    plt.tight_layout()
    plt.savefig("plots/price_rating_scatter.png")
    plt.close()

print("\nAnalysis completed successfully!")
print("Check the output and plots folders.")

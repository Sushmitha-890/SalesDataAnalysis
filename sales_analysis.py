# Step 1: Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load the Dataset
df = pd.read_csv("sales_data.csv")

# Display the first few rows of the dataset
print("Dataset Preview:")
print(df.head())

# Step 3: Check for Missing Values
print("\nMissing Values Count:")
print(df.isnull().sum())

# Handle missing values by filling with zero
df.fillna(0, inplace=True)

# Step 4: Analyze Best-Selling Products
best_sellers = df.groupby("Product Name")["Sales"].sum().reset_index()
best_sellers = best_sellers.sort_values(by="Sales", ascending=False)

print("\nTop 5 Best-Selling Products:")
print(best_sellers.head())

# Step 5: Convert Order Date Column to DateTime Format
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True, errors='coerce')

# Step 6: Aggregate Monthly Sales
monthly_sales = df.resample("ME", on="Order Date")["Sales"].sum()

# Step 7: Plot Best-Selling Products (Bar Chart)
plt.figure(figsize=(10, 5))
sns.barplot(x="Product Name", y="Sales", hue="Product Name", data=best_sellers.head(10), palette="coolwarm", legend=False)

plt.xticks(rotation=45)
plt.title("Top 10 Best-Selling Products")
plt.xlabel("Product Name")
plt.ylabel("Total Sales")
plt.savefig("top_selling_products.png", dpi=300, bbox_inches="tight")

plt.show()

# Step 8: Plot Monthly Sales Trend (Line Chart)
plt.figure(figsize=(10, 5))
plt.plot(monthly_sales.index, monthly_sales.values, marker="o", linestyle="-", color="b")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid()
plt.show()

# 📌 Step 9: Sales by Category (NEW ADDITION)
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 6))
sns.barplot(x=category_sales.index, y=category_sales.values, palette="viridis")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.title("Sales by Category")
plt.xticks(rotation=45)
plt.show()

# 📌 Step 10: Top 10 Cities with Highest Sales (NEW ADDITION)
top_cities = df.groupby("City")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 5))
sns.barplot(x=top_cities.index, y=top_cities.values, palette="magma")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.title("Top 10 Cities with Highest Sales")
plt.xticks(rotation=45)
plt.show()

# Step 11: Save the Cleaned Dataset
df.to_csv("cleaned_sales_data.csv", index=False)
print("\nCleaned dataset saved as 'cleaned_sales_data.csv'!")
plt.show(block=True)



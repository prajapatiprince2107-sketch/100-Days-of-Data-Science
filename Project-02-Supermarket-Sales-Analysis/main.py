# ==========================================
# PROJECT 02: SUPERMARKET SALES ANALYSIS
# Author: Prince
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


# ==========================================
# 1. LOAD DATASET
# ==========================================

BASE_DIR = Path(__file__).resolve().parent

df = pd.read_csv(BASE_DIR / "data" / "sales.csv")

print("=" * 50)
print("       SUPERMARKET SALES ANALYSIS")
print("=" * 50)

print("\n1. ORIGINAL DATASET")
print(df)


# ==========================================
# 2. DATASET INFORMATION
# ==========================================

print("\n2. DATASET INFORMATION")

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())


# ==========================================
# 3. CALCULATE TOTAL SALES
# ==========================================

df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

print("\n3. DATA WITH TOTAL SALES")
print(df)


# ==========================================
# 4. TOTAL REVENUE
# ==========================================

total_revenue = df["Total_Sales"].sum()

print("\n4. TOTAL REVENUE")
print(f"Total Revenue: {total_revenue:,.2f}")


# ==========================================
# 5. CATEGORY-WISE SALES ANALYSIS
# ==========================================

category_sales = (
    df.groupby("Category")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n5. CATEGORY-WISE SALES")
print(category_sales)

best_category = category_sales.idxmax()

print("\nBest-Selling Category:", best_category)


# ==========================================
# 6. BRANCH-WISE SALES ANALYSIS
# ==========================================

branch_sales = (
    df.groupby("Branch")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n6. BRANCH-WISE SALES")
print(branch_sales)

best_branch = branch_sales.idxmax()

print("\nBest Performing Branch:", best_branch)


# ==========================================
# 7. PAYMENT METHOD ANALYSIS
# ==========================================

payment_counts = df["Payment"].value_counts()

print("\n7. PAYMENT METHOD USAGE")
print(payment_counts)

popular_payment = payment_counts.idxmax()

print("\nMost Popular Payment Method:", popular_payment)


# ==========================================
# 8. QUANTITY SOLD BY CATEGORY
# ==========================================

category_quantity = (
    df.groupby("Category")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\n8. QUANTITY SOLD BY CATEGORY")
print(category_quantity)


# ==========================================
# 9. CATEGORY-WISE SALES BAR CHART
# ==========================================

plt.figure(figsize=(10, 6))

sns.barplot(
    x=category_sales.index,
    y=category_sales.values
)

plt.title("Category-wise Supermarket Sales")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=15)

plt.tight_layout()

plt.savefig(BASE_DIR / "category_sales.png", dpi=300)

plt.show()


# ==========================================
# 10. BRANCH-WISE SALES BAR CHART
# ==========================================

plt.figure(figsize=(8, 5))

sns.barplot(
    x=branch_sales.index,
    y=branch_sales.values
)

plt.title("Branch-wise Sales Comparison")
plt.xlabel("Branch")
plt.ylabel("Total Sales")

plt.tight_layout()

plt.savefig(BASE_DIR / "branch_sales.png", dpi=300)

plt.show()


# ==========================================
# 11. PAYMENT METHOD PIE CHART
# ==========================================

plt.figure(figsize=(8, 6))

plt.pie(
    payment_counts.values,
    labels=payment_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Payment Method Distribution")

plt.tight_layout()

plt.savefig(BASE_DIR / "payment_methods.png", dpi=300)

plt.show()


# ==========================================
# 12. SAVE ANALYSIS RESULTS
# ==========================================

output_file = BASE_DIR / "data" / "sales_analysis_results.csv"

df.to_csv(output_file, index=False)

print("\n12. RESULTS SAVED")
print("Results file:", output_file)


# ==========================================
# 13. FINAL SUMMARY
# ==========================================

print("\n" + "=" * 50)
print("              FINAL SUMMARY")
print("=" * 50)

print(f"Total Transactions: {len(df)}")
print(f"Total Revenue: {total_revenue:,.2f}")
print(f"Best-Selling Category: {best_category}")
print(f"Best Performing Branch: {best_branch}")
print(f"Most Popular Payment: {popular_payment}")

print("\nAll analyses completed successfully!")
print("=" * 50)
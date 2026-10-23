import pandas as pd

#load the og dataset
df = pd.read_excel("Online Retail.xlsx")
# #explore dataset
# print("Dataset dimensions:", df.shape)

# print("\nColumn names:")
# print(df.columns.tolist())

# print("\nFirst 10 rows:")
# print(df.head(10))

# print("\nData types and missing values:")
# df.info()

# print("\nMissing values per column:")
# print(df.isna().sum())

# print("\nExact duplicate rows:")
# print(df.duplicated().sum())

# print("\nQuantity statistics:")
# print(df["Quantity"].describe())

# print("\nUnitPrice statistics:")
# print(df["UnitPrice"].describe())

# print("\nInvoice date range:")
# print(df["InvoiceDate"].min())
# print(df["InvoiceDate"].max())


# print("\n--- DATA QUALITY INVESTIGATION ---")

# # 1. Investigate quantities
# print("\nNegative quantities:", (df["Quantity"] < 0).sum())
# print("Zero quantities:", (df["Quantity"] == 0).sum())

# # 2. Investigate prices
# print("\nNegative prices:", (df["UnitPrice"] < 0).sum())
# print("Zero prices:", (df["UnitPrice"] == 0).sum())

# # 3. Investigate cancelled invoices
# cancelled = df["InvoiceNo"].astype(str).str.startswith("C")
# print("\nRows with cancellation invoice numbers:", cancelled.sum())
# print("Examples of cancelled invoices:")
# print(df[cancelled].head(10))

# # 4. Inspect examples of exact duplicates
# print("\nExamples of duplicate rows:")
# print(df[df.duplicated(keep=False)].head(10))

# # 5. Inspect rows with missing descriptions
# print("\nExamples with missing descriptions:")
# print(df[df["Description"].isna()].head(10))

# # 6. Calculate a preliminary line amount
# df["LineAmount"] = df["Quantity"] * df["UnitPrice"]

# print("\nTotal line amount before cleaning:")
# print(round(df["LineAmount"].sum(), 2))


# print("\n--- INVESTIGATING EXCEPTIONS ---")

# # 1. Check negative quantities
# print("\nNegative quantities:")
# print((df["Quantity"] < 0).sum())

# print("\nNegative quantities with cancellation invoice numbers:")
# negative_qty = df["Quantity"] < 0
# cancelled = df["InvoiceNo"].astype(str).str.startswith("C")
# print((negative_qty & cancelled).sum())

# print("\nNegative quantities without cancellation invoice numbers:")
# print((negative_qty & ~cancelled).sum())

# # 2. Inspect zero-price transactions
# print("\nExamples of zero-price transactions:")
# print(
#     df.loc[df["UnitPrice"] == 0,
#            ["InvoiceNo", "StockCode", "Description",
#             "Quantity", "UnitPrice"]]
#     .head(10)
#     .to_string(index=False)
# )

# # 3. Inspect negative-price transactions
# print("\nTransactions with negative prices:")
# print(
#     df.loc[df["UnitPrice"] < 0,
#            ["InvoiceNo", "StockCode", "Description",
#             "Quantity", "UnitPrice"]]
#     .to_string(index=False)
# )

# # 4. Inspect exact duplicate rows
# print("\nExamples of exact duplicate rows:")
# print(
#     df.loc[df.duplicated(keep=False)]
#     .sort_values(by=["InvoiceNo", "StockCode"])
#     .head(10)
#     .to_string(index=False)
# )


# print("\n--- DUPLICATE IMPACT ANALYSIS ---")

# # Count exact duplicate rows after their first occurrence
# duplicate_count = df.duplicated().sum()
# print("Exact duplicate rows to potentially remove:", duplicate_count)

# # Compare dataset size before and after removing exact duplicates
# df_deduplicated = df.drop_duplicates()

# print("Rows before:", len(df))
# print("Rows after removing exact duplicates:", len(df_deduplicated))
# print("Rows removed:", len(df) - len(df_deduplicated))

# # Compare the total line amount before and after deduplication
# df["LineAmount"] = df["Quantity"] * df["UnitPrice"]
# df_deduplicated = df_deduplicated.copy()
# df_deduplicated["LineAmount"] = (
#     df_deduplicated["Quantity"] * df_deduplicated["UnitPrice"]
# )

# print("\nTotal line amount before deduplication:")
# print(round(df["LineAmount"].sum(), 2))

# print("\nTotal line amount after deduplication:")
# print(round(df_deduplicated["LineAmount"].sum(), 2))

# print("\nDifference in total line amount:")
# print(round(
#     df["LineAmount"].sum() -
#     df_deduplicated["LineAmount"].sum(), 2
# ))


# print("\n--- MISSING VALUE INVESTIGATION ---")

# # 1. Count rows with missing customer IDs and descriptions
# missing_customer = df["CustomerID"].isna()
# missing_description = df["Description"].isna()

# print("Missing CustomerID:", missing_customer.sum())
# print("Missing Description:", missing_description.sum())

# # 2. Check missing CustomerID by transaction type
# cancelled = df["InvoiceNo"].astype(str).str.startswith("C")
# negative_qty = df["Quantity"] < 0
# zero_price = df["UnitPrice"] == 0

# print("\nRows with missing CustomerID that are cancellations:")
# print((missing_customer & cancelled).sum())

# print("\nRows with missing CustomerID and negative quantity:")
# print((missing_customer & negative_qty).sum())

# print("\nRows with missing CustomerID and zero price:")
# print((missing_customer & zero_price).sum())

# # 3. Inspect rows with missing descriptions
# print("\nExamples with missing descriptions:")
# print(
#     df.loc[
#         missing_description,
#         ["InvoiceNo", "StockCode", "Quantity",
#          "InvoiceDate", "UnitPrice", "CustomerID", "Country"]
#     ].head(10).to_string(index=False)
# )

# # 4. Check whether missing descriptions have zero prices
# print("\nMissing descriptions with zero price:")
# print((missing_description & zero_price).sum())

# print("\nMissing descriptions with nonzero price:")
# print((missing_description & ~zero_price).sum())


# print("\n--- TRANSACTION CATEGORY SUMMARY ---")

# cancelled = df["InvoiceNo"].astype(str).str.startswith("C")
# negative_qty = df["Quantity"] < 0
# zero_price = df["UnitPrice"] == 0
# negative_price = df["UnitPrice"] < 0
# missing_description = df["Description"].isna()

# categories = {
#     "All rows": pd.Series(True, index=df.index),
#     "Cancellation invoice rows": cancelled,
#     "Negative quantity rows": negative_qty,
#     "Negative quantity without cancellation invoice": (
#         negative_qty & ~cancelled
#     ),
#     "Zero-price rows": zero_price,
#     "Negative-price rows": negative_price,
#     "Missing description rows": missing_description,
#     "Missing description and zero price": (
#         missing_description & zero_price
#     ),
# }

# for category, mask in categories.items():
#     print(f"{category}: {mask.sum():,}")

# # Summarize the preliminary line amount by transaction type
# df["LineAmount"] = df["Quantity"] * df["UnitPrice"]

# print("\nLine amount for cancellation invoice rows:")
# print(round(df.loc[cancelled, "LineAmount"].sum(), 2))

# print("\nLine amount for negative quantities without cancellation:")
# print(round(df.loc[negative_qty & ~cancelled, "LineAmount"].sum(), 2))

# print("\nLine amount for zero-price rows:")
# print(round(df.loc[zero_price, "LineAmount"].sum(), 2))

# print("\nLine amount for negative-price rows:")
# print(round(df.loc[negative_price, "LineAmount"].sum(), 2))


print("\n--- BASELINE SALES SUMMARY ---")

# Preliminary totals before applying cleaning rules
df["LineAmount"] = df["Quantity"] * df["UnitPrice"]

print("Total rows:", len(df))
print("Unique invoices:", df["InvoiceNo"].nunique())
print("Unique products:", df["StockCode"].nunique())
print("Unique countries:", df["Country"].nunique())
print("Unique identified customers:", df["CustomerID"].nunique())

print("\nTotal quantity:")
print(df["Quantity"].sum())

print("\nTotal preliminary line amount:")
print(round(df["LineAmount"].sum(), 2))

print("\nTop 10 countries by number of rows:")
print(df["Country"].value_counts().head(10).to_string())

print("\nTop 10 products by number of rows:")
print(df["StockCode"].value_counts().head(10).to_string())

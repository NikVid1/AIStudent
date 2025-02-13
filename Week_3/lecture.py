# /// script
# dependencies = [
#   "numpy",
#   "pandas",
# ]
# ///

import pandas as pd
import numpy as np

# Create the DataFrame.
data = {
    "week": ["2025-01-13", "2025/01/13", "2025-01-05", "2024-12-30", "2024-12-23"],
    "remaining_inventory": [3, 10, 18, 0, 400],
    "product": ["null", "product_a", "product_a", "product_a", "product_a"]
}
df = pd.DataFrame(data)

# Replace string "null" with an actual missing value so that pandas can handle it.
df["product"] = df["product"].replace("null", np.nan)

print("Original DataFrame:")
print(df)



### 1. Convert the week column to datetime.
# for all yyyy/mm/dd formats convert to yyyy-mm-dd
df["week"] = df["week"].apply(lambda x: pd.to_datetime(x, format="%Y/%m/%d") if "/" in x else pd.to_datetime(x))

### 2. Edit 2025-01-05 to be a 2025-01-06 due ot data entry error.
df.loc[df["week"] == "2025-01-05", "week"] = "2025-01-06"

### 3. Talk to the purchasing team to find out why 400 units are remaining
# turns out its a data entry error and should be 40, so we fix it
df.loc[df["remaining_inventory"] == 400, "remaining_inventory"] = 40

### 4. Talk to the sales team to find out why the product is null
# turns out its a data revised manually after the week and should be product_a, so we fix it
df.loc[df["product"] == np.nan, "product"] = "product_a"

### 5. We now have two rows with the same week so we need to group by week and sum the inventory
df = df.groupby("week")["remaining_inventory"].sum().reset_index()

df = df.sort_values("week", ascending=False)
print("\nCleaned DataFrame:")
print(df)




### PANDAS EQUIVALENT OF SQL
import pandas as pd

sales_data = {
    "product_id": ["product_a", "product_a", "product_b"],
    "sales": [8, 3, 1],
    "date": ["2025-01-06", "2025-01-05", "2025-01-04"]
}

pricing_data = {
    "product_id": ["product_a", "product_b"],
    "price": [10, 25]
}

sales_df = pd.DataFrame(sales_data)
pricing_df = pd.DataFrame(pricing_data)

# Perform JOIN (equivalent to SQL JOIN ON product_id)
merged_df = sales_df.merge(pricing_df, on="product_id", how="inner")

# Compute total revenue
result_df = merged_df.groupby(["product_id", "price"])["sales"].sum().reset_index()
result_df["total_revenue"] = result_df["sales"] * result_df["price"]
result_df = result_df.drop(columns=["sales"])
print(result_df)
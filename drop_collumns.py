import pandas as pd

# Load the data
file_path = "DriverIDWash_2023_2024_with_State_Country.csv"
df = pd.read_csv(file_path)

# Columns to drop
columns_to_drop = ["ISO Numeric Code", "Country"]

# Drop the specified columns
df = df.drop(columns=columns_to_drop)

# Save the modified dataframe back to the same file
df.to_csv(file_path, index=False)

print("Columns dropped and file updated successfully!")

import pandas as pd
from tqdm import tqdm

file_name = "Vehicle_Registration_Transactions_by_Department_of_Licensing_20241121.csv"
NYS_driver_license_in_WA = pd.read_csv("Surrendered_NYS_driver_license_in_WA.csv")
df = pd.read_csv(file_name)

print(f"Number of rows: {len(df)}")
print(f"Number of unique Vehicle Types: {df['Vehicle Type'].nunique()}")
print(f"Unique Vehicle Types: {df['Vehicle Type'].unique()}")
print(f"Number of unique Vehicle Primary Uses: {df['Vehicle Primary Use'].nunique()}")
city_counts = df['City'].value_counts()
NYS_driver_license_in_WA_City_counts = NYS_driver_license_in_WA['City'].value_counts()
print("Number of registrations per city:")
print(city_counts)

print("Number of NYS driver licenses per city:")
print(NYS_driver_license_in_WA_City_counts)

print("Bottom 50 cities by number of NYS driver licenses:")
print(NYS_driver_license_in_WA_City_counts.tail(50))

import pandas as pd
from tqdm import tqdm
import re

# Load the dataset
df = pd.read_csv("DriverIDWash_2023_2024_with_State_Country.csv")

# Filter for people from New York State and "Driver License" card type
ny_df = df[(df['State_y'] == 'New York') & (df['Card Type Issued'] == 'Driver License') & (df['County of Residence'] == "King")]

# Function to extract latitude and longitude from "Card Origin"
def extract_coordinates(card_origin):
    match = re.search(r"POINT \(([-\d\.]+) ([-\d\.]+)\)", card_origin)
    if match:
        lon, lat = map(float, match.groups())
        return lat, lon
    return None, None

# Extract latitude and longitude into separate columns for New York entries
ny_df[['Latitude', 'Longitude']] = ny_df['Card Origin'].apply(lambda x: pd.Series(extract_coordinates(x)))

# Remove duplicate coordinates to reduce geocoding workload
unique_coords = ny_df[['Latitude', 'Longitude']].drop_duplicates()

# Merge the results back to the original New York DataFrame
ny_df = ny_df.merge(unique_coords, on=['Latitude', 'Longitude'], how='left')

# Drop Latitude and Longitude columns if no longer needed
ny_df = ny_df.drop(columns=['Latitude', 'Longitude'])

# Save the updated New York DataFrame
ny_df.to_csv("DriverIDWash_2023_2024_NewYork_DriverLicenses.csv", index=False)

# Print a sample of the updated DataFrame
print(ny_df.head())

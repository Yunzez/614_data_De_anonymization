import pandas as pd
from geopy.geocoders import Nominatim
from tqdm import tqdm  # For progress bar

# Load the dataset
df = pd.read_csv("DriverIDWash_2023_2024.csv")

# Initialize Geolocator
geolocator = Nominatim(user_agent="reverse_geocoder")

# Function to get State and Country from coordinates (exclude City)
def get_state_country(lat, lon):
    try:
        location = geolocator.reverse((lat, lon), exactly_one=True)
        address = location.raw.get('address', {})
        state = address.get('state', 'Unknown')
        country = address.get('country', 'Unknown')
        return state, country
    except Exception:
        return "Unknown", "Unknown"

# Create a cache to store already processed coordinates
cache = {}

def get_state_country_cached(lat, lon):
    coord = (lat, lon)
    if coord in cache:
        return cache[coord]
    else:
        result = get_state_country(lat, lon)
        cache[coord] = result
        return result

# Remove duplicate coordinates to reduce geocoding workload
unique_coords = df[['Latitude', 'Longitude']].drop_duplicates()

# Apply geocoding to unique coordinates
tqdm.pandas()  # Add progress bar to track progress
unique_coords[['State', 'Country']] = unique_coords.progress_apply(
    lambda row: get_state_country_cached(row['Latitude'], row['Longitude']), axis=1, result_type="expand"
)

# Merge the results back to the original DataFrame
df = df.merge(unique_coords, on=['Latitude', 'Longitude'], how='left')

# Drop Latitude and Longitude columns if no longer needed
df = df.drop(columns=['Latitude', 'Longitude'])

# Save the updated DataFrame
df.to_csv("DriverIDWash_2023_2024_with_State_Country.csv", index=False)

# Print a sample of the updated DataFrame
print(df.head())
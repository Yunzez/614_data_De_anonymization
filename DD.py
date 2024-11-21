import pandas as pd
from geopy.geocoders import Nominatim

# Load the dataset
df = pd.read_csv("DriverIDWash.csv")

# Filter for 2023-2024 data only
df = df[df['Year'].isin([2023, 2024])]

# Parse 'Card Origin' into Latitude and Longitude
df[['Longitude', 'Latitude']] = df['Card Origin'].str.extract(r'POINT \(([^ ]+) ([^ ]+)\)').astype(float)

print("Latitude, longitude columns created")
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
    except Exception as e:
        return "Unknown", "Unknown"

print("geocoding done.")

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

# Apply the function to add 'State' and 'Country' columns
# Apply the function with caching
#  
# Save the updated DataFrame
df.to_csv("DriverIDWash_2023_2024_with_State_Country.csv", index=False)

# Print a sample of the updated DataFrame
print(df.head())
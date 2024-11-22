import pandas as pd
from tqdm import tqdm

# Load the dataset
file_name = "NYS_driver_license_in_WA.csv"
df = pd.read_csv(file_name)
# Filter the dataframe by City

cities = [
    "Algona",
    "Auburn",
    "Beaux Arts Village",
    "Bellevue",
    "Black Diamond",
    "Bothell",
    "Burien",
    "Carnation",
    "Clyde Hill",
    "Covington",
    "Des Moines",
    "Duvall",
    "Enumclaw",
    "Federal Way",
    "Hunts Point",
    "Issaquah",
    "Kenmore",
    "Kent",
    "Kirkland",
    "Lake Forest Park",
    "Maple Valley",
    "Medina",
    "Mercer Island",
    "Milton",
    "Newcastle",
    "Normandy Park",
    "North Bend",
    "Pacific",
    "Redmond",
    "Renton",
    "Sammamish",
    "SeaTac",
    "Seattle",
    "Shoreline",
    "Skykomish",
    "Snoqualmie",
    "Tukwila",
    "Woodinville",
    "Yarrow Point"
]

cities_lower = [city.lower() for city in cities]  # Convert all cities to lowercase

# Ensure 'City' column is lowercase for comparison
df['City'] = df['City'].str.lower()

# Filter the dataframe by cities
filtered_df = df[df['City'].isin(cities_lower)]

# Further filter the dataframe by License Class
filtered_df = filtered_df[filtered_df['License Class'] == 'D']

# Save the filtered dataframe to a new CSV file
filtered_df.to_csv("Filtered_NYS_driver_license_in_king.csv", index=False)




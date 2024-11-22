import pandas as pd
from tqdm import tqdm

# Load the dataset
file_name = "Vehicle_Registration_Transactions_by_Department_of_Licensing_20241121.csv"
df = pd.read_csv(file_name)

# Ensure the Transaction Date column is in datetime format
df['Transaction Month and Year'] = pd.to_datetime(df['Transaction Month and Year'], errors='coerce')

# Define the date range for filtering
start_date = pd.Timestamp("2023-2-1")
end_date = pd.Timestamp("2025-01-01")

# Create a dictionary for postal code to city mapping
postal_code_to_city = {
    98052: "Redmond", 98115: "Seattle", 98034: "Kirkland", 98103: "Seattle", 
    98003: "Federal Way", 98133: "Seattle", 98023: "Federal Way", 98092: "Auburn",
    98105: "Seattle", 98042: "Kent", 98118: "Seattle", 98125: "Seattle", 
    98058: "Renton", 98059: "Renton", 98031: "Kent", 98122: "Seattle", 
    98033: "Kirkland", 98006: "Bellevue", 98004: "Bellevue", 98032: "Kent", 
    98198: "Seattle", 98030: "Kent", 98038: "Maple Valley", 98002: "Auburn", 
    98056: "Renton", 98117: "Seattle", 98001: "Auburn", 98155: "Seattle", 
    98168: "Seattle", 98144: "Seattle", 98109: "Seattle", 98029: "Issaquah",
    98074: "Sammamish", 98106: "Seattle", 98107: "Seattle", 98146: "Seattle",
    98027: "Issaquah", 98116: "Seattle", 98011: "Bothell", 98007: "Bellevue",
    98188: "Seattle", 98008: "Bellevue", 98178: "Seattle", 98119: "Seattle",
    98102: "Seattle", 98040: "Mercer Island", 98075: "Sammamish", 
    98072: "Woodinville", 98055: "Renton", 98108: "Seattle", 98028: "Kenmore", 
    98112: "Seattle", 98053: "Redmond", 98166: "Seattle", 98199: "Seattle",
    98022: "Enumclaw", 98005: "Bellevue", 98177: "Seattle", 98126: "Seattle",
    98121: "Seattle", 98136: "Seattle", 98101: "Seattle", 98065: "Snoqualmie",
    98045: "North Bend", 98104: "Seattle", 98077: "Woodinville", 98057: "Renton",
    98019: "Duvall", 98070: "Vashon", 98148: "Seattle", 98014: "Carnation",
    98047: "Pacific", 98010: "Black Diamond", 98024: "Fall City", 
    98051: "Ravensdale", 98039: "Medina", 98195: "Seattle", 98134: "Seattle",
    98164: "Seattle", 98224: "Baring", 98288: "Skykomish", 98050: "Preston",
    98174: "Seattle", 98158: "Seattle", 98154: "Seattle", 98025: "Hobart"
}

# Add a 'City' column based on 'Postal Code'
df['City'] = df['Postal Code'].map(postal_code_to_city)

# Apply filtering with tqdm progress bar
tqdm.pandas(desc="Filtering Transactions")
filtered_df = df.progress_apply(
    lambda row: (
        start_date < row['Transaction Month and Year'] < end_date and
        row['Vehicle Type'] in ["PASSENGER CAR", "MULTIPURPOSE PASSENGER VEHICLE (MPV)"] and
        row['Vehicle Primary Use'] == "Passenger Vehicle" and
        row['County'] == "King" and
        row["Model Year"] >= 2010 and
        row["Owner Type"] == "Individual Owner" and
        (row["Transaction Type"] == "Original Registration" or row["Transaction Type"] == "Registration at time of Transfer")
    ), 
    axis=1
) 

# Use the boolean mask to filter the DataFrame
filtered_df = df[filtered_df]

# Save the filtered DataFrame back to the same file
filtered_df.to_csv(file_name, index=False)

# Print the head of the filtered DataFrame
print(filtered_df.head())

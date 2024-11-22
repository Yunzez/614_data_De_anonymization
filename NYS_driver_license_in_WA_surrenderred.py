import pandas as pd
from tqdm import tqdm

file_name = "NYS_driver_license_in_WA.csv"
df = pd.read_csv(file_name)
df = df[df['Status'] == 'SURRENDERED']
# Calculate the estimated Year of Issue based on Year of Expiration
df['Year of Issue (Estimated)'] = df['Year of Expiration'] - 8

# Estimate the year of moving to Washington
# Assume most people move near the expiration year
df['Year of Move (Estimated)'] = df['Year of Expiration'] - 1  # Adjust as needed

# Filter records for individuals who likely moved to Washington recently
df = df[df['Year of Move (Estimated)'] >= 2022]  # Adjust year threshold

output_file_name = "Surrendered_NYS_driver_license_in_WA.csv"
df.to_csv(output_file_name, index=False)
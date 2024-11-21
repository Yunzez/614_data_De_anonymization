import pandas as pd

# Load the updated dataset with State and Country information
df = pd.read_csv("DriverIDWash_2023_2024_with_State_Country.csv")

# Group by Country and State and calculate counts
grouped_data = df.groupby(['Country', 'State_y']).size().reset_index(name='Count')

# Sort the grouped data by Count in descending order
sorted_data = grouped_data.sort_values(by='Count', ascending=False)

# Display the top 10 entries
print(sorted_data.head(10))

# Save the grouped data to a CSV file for further analysis
sorted_data.to_csv("Grouped_By_Country_and_State.csv", index=False)

grouped_data_country = df.groupby(['Country']).size().reset_index(name='Count')
sorted_data_country = grouped_data_country.sort_values(by='Count', ascending=False)
sorted_data_country.to_csv("Grouped_By_Country.csv", index=False)
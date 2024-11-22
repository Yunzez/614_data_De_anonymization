# trying to make correlation here 

import pandas as pd
vehicle_reg_data = pd.read_csv("Vehicle_Registration_Transactions_by_Department_of_Licensing_20241121.csv")
id_ny_in_king = pd.read_csv("DriverIDWash_2023_2024_NewYork_in_King.csv")
surrendered_ny = pd.read_csv("Surrendered_NYS_driver_license_in_WA.csv")

surrendered_ny_carnation = surrendered_ny[surrendered_ny['City'] == 'CARNATION']
print(surrendered_ny_carnation)

vehicle_reg_carnation = vehicle_reg_data[vehicle_reg_data['City'] == 'Carnation']
# print(vehicle_reg_carnation)

make_counts = vehicle_reg_carnation['Make'].value_counts().reset_index(name='Count')
make_counts.columns = ['Make', 'Count']
print(make_counts)


grouped_data = id_ny_in_king.groupby(['Year', 'Month Number']).size().reset_index(name='Count')
print(grouped_data)
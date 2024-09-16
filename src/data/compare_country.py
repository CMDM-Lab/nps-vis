import pandas as pd

# Load the Excel and CSV files
pop_file = 'population.csv'
nps_file = 'processed_nps_complete_list.csv'

# Read the Excel and CSV files into DataFrames
pop_df = pd.read_csv(pop_file)
nps_df = pd.read_csv(nps_file)

# Extract the 'Country Code' from the Excel and 'iso_alpha' from the CSV
excel_country_codes = pop_df['iso_alpha'].astype(str)
csv_iso_alpha = nps_df['iso_alpha'].astype(str)

# Find the unique 'iso_alpha' values in the CSV that are not present in the 'Country Code' in the Excel
unique_missing_in_excel = csv_iso_alpha[~csv_iso_alpha.isin(excel_country_codes)].unique()

# Print the unique mismatches and their count
print("Unique iso_alpha values in population file not found in nps 'Country Code':")
print(unique_missing_in_excel)
print(f"Total number of unique iso_alpha values not in population file: {len(unique_missing_in_excel)}")
#Unique iso_alpha values in population file not found in nps 'Country Code':['TWN' 'MYT']
#Total number of unique iso_alpha values not in population file: 2
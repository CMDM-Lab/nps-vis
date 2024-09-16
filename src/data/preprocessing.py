import pandas as pd
import pycountry
import pycountry_convert as pc

# Custom mapping for countries with missing or incorrect ISO codes
custom_country_mapping = {
    "TURKEY": "TUR",
    "REPUBLIC OF KOREA": "KOR",
    "NORTH MACEDONIA, REPUBLIC OF": "MKD",
    "VIETNAM": "VNM",
    "ISLAMIC REPUBLIC OF IRAN": "IRN",
    "MACAO (CHINA)" : "MAC",
    "TÜRKIYE, REPUBLIC OF" : "TUR",
    "HONG KONG (CHINA)" : "HKG",
    "BOLIVIA" : "BOL",
    "PALESTINIAN TERRITORY, OCCUPIED" : "PSE"
}

# Function to get ISO alpha-3 code with custom mapping fallback
def get_iso_alpha3(country_name):
    # Try to get the ISO code using pycountry
    try:
        return pycountry.countries.get(name=country_name).alpha_3
    except:
        # If pycountry lookup fails, fallback to custom mapping
        return custom_country_mapping.get(country_name, None)

# Function to get continent name from country code
def country_to_continent(country_code):
    try:
        continent_code = pc.country_alpha2_to_continent_code(pc.country_alpha3_to_country_alpha2(country_code))
        return pc.convert_continent_code_to_continent_name(continent_code)
    except:
        return None

# Function to group data, clean country names, and add ISO alpha codes
def group_data(data):
    # Strip trailing spaces from 'Country' column
    data['Country'] = data['Country'].str.strip()

    # Group the data by 'Country' and 'Year', count the occurrences, and get the first 'Group Name'
    grouped_data = data.groupby(['Country', 'Year', 'Group Name']).agg({
        'Country': 'size'       # Count the number of occurrences
    }).rename(columns={'Country': 'count'}).reset_index()

    # Apply ISO alpha-3 code mapping to the 'Country' column
    grouped_data['iso_alpha'] = grouped_data['Country'].apply(get_iso_alpha3)

    # Apply continent mapping
    grouped_data['Continent'] = grouped_data['iso_alpha'].apply(country_to_continent)

    grouped_data = grouped_data.sort_values(by='Year')

    return grouped_data


def add_total_year(data, output_file_path):
    # Grouping the data by Country and Group Name and summing the count
    grouped_data = data.groupby(['Country', 'Group Name', 'iso_alpha', 'Continent']).agg({'count': 'sum'}).reset_index()

    # Adding a marker for the aggregated rows
    grouped_data['Year'] = 'Total'

    # Concatenating the original data with the aggregated data
    combined_data = pd.concat([data, grouped_data], ignore_index=True)
    print(combined_data.head())

    # Save the new DataFrame to a CSV file
    combined_data.to_csv(output_file_path, index=False)

    print(f"File saved to {output_file_path}")



# Use the function 'group_data' to process your data and save to a CSV file
file_path = './nps_complete_list.csv'  # Replace with the path to your CSV file
output_file_path = './processed_nps_complete_list.csv'  # Replace with your desired output file path
data = pd.read_csv(file_path)
grouped_dataframe = group_data(data)
add_total_year(grouped_dataframe, output_file_path)

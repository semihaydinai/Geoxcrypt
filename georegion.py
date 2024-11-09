import pandas as pd
import json
import os
from opencage.geocoder import OpenCageGeocode

# Enter your OpenCage API key here
# OpenCage API key voor hier invullen
API_KEY = 'YOUR_OPENCAGE_API_KEY'
geocoder = OpenCageGeocode(API_KEY)

# Load the Excel file
# Laad het Excel-bestand
data = pd.read_excel("your_excel_file.xlsx")  # Update the file name here / Werk hier de bestandsnaam bij

# Add 'Country', 'Region', and 'County/City' columns and leave them empty
# Voeg de kolommen 'Country', 'Region' en 'County/City' toe en laat ze leeg
data['Country'] = None
data['Region'] = None
data['County/City'] = None

# Function to get country, region, and county/city information
# Functie om land, regio en county/stad informatie op te halen
def get_location_info(lat, lon):
    try:
        result = geocoder.reverse_geocode(lat, lon, language='en')
        if result and 'country' in result[0]['components']:
            country = result[0]['components']['country']
            region = result[0]['components'].get('state', None)  # Region information / Regio informatie
            county_city = result[0]['components'].get('county', None) or result[0]['components'].get('city', None)  # County/City information / County/Stad informatie
            return country, region, county_city
    except Exception as e:
        print(f"Error: {e}")  # Hata / Fout
    return None, None, None

# Process the data
# Verwerk de gegevens
for index, row in data.iterrows():
    cell_location = row['Cell Location']
    
    # Check if 'Cell Location' cell is not empty
    # Controleer of de cel 'Cell Location' niet leeg is
    if pd.notna(cell_location):
        try:
            # Parse JSON format
            # JSON-formaat parseren
            location_data = json.loads(cell_location)
            lat = location_data["Lat"]
            lon = location_data["Lon"]
            
            # Retrieve country, region, and county/city and write to relevant columns
            # Haal land, regio en county/stad op en schrijf in relevante kolommen
            country, region, county_city = get_location_info(lat, lon)
            data.at[index, 'Country'] = country
            data.at[index, 'Region'] = region
            data.at[index, 'County/City'] = county_city
        except (json.JSONDecodeError, KeyError, TypeError) as e:
            print(f"Row {index} error: {e}")  # Satır hatası / Rij fout

# Generate a unique filename if a file with the same name already exists
# Genereer een unieke bestandsnaam als er al een bestand met dezelfde naam bestaat
def generate_unique_filename(filename):
    base, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(new_filename):
        new_filename = f"{base}({counter}){extension}"
        counter += 1
    return new_filename

# Save the result to a new file
# Sla het resultaat op in een nieuw bestand
output_filename = generate_unique_filename("your_excel_file_with_location_info.xlsx")
data.to_excel(output_filename, index=False)
print("Country, region, and county/city information successfully added.") 
# Land, regio en county/stad informatie succesvol toegevoegd.

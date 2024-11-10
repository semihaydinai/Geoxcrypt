# Geocoding Excel Data with Country, Region, and City Information

This script enriches an Excel file with country, region, and county/city information based on latitude and longitude data using the OpenCage Geocoding API.

Dit script verrijkt een Excel-bestand met informatie over land, regio en county/stad op basis van breedte- en lengtegraadgegevens met behulp van de OpenCage Geocoding API.

---

## Requirements / Vereisten

1. Python 3.x
2. An OpenCage API key / Een OpenCage API-sleutel

---

## Installation / Installatie

1. Clone this repository and navigate to the project directory.
   
   Dit project klonen en naar de projectmap navigeren.

   ```bash
   git clone <repository-url>
   cd <repository-directory>

# Install the required Python packages:

De benodigde Python-pakketten installeren:

pip install -r requirements.txt

# Setup / Instellen

Open the script file and replace 'YOUR_OPENCAGE_API_KEY' with your actual OpenCage API key.

Open het scriptbestand en vervang 'YOUR_OPENCAGE_API_KEY' door je eigen OpenCage API-sleutel.

Place your input Excel file in the project directory and update the filename in the script:

Plaats het invoer-Excel-bestand in de projectmap en werk de bestandsnaam in het script bij:

data = pd.read_excel("your_excel_file.xlsx")  # Update file name here / Werk bestandsnaam hier bij

# Usage / Gebruik
Run the script to add country, region, and county/city information to each row based on the coordinates in the Cell Location column.

Voer het script uit om land-, regio- en county/stad-informatie toe te voegen aan elke rij op basis van de coördinaten in de kolom Cell Location.

python georegion.py

The script will automatically save the updated file with a unique name if a file with the same name already exists.

Het script slaat het bijgewerkte bestand automatisch op met een unieke naam als er al een bestand met dezelfde naam bestaat.

# Output / Resultaat
The updated Excel file will contain three new columns: Country, Region, and County/City.

Het bijgewerkte Excel-bestand bevat drie nieuwe kolommen: Country, Region en County/City.

# Notes / Opmerkingen
Make sure your input data includes a Cell Location column with JSON data for latitude and longitude.

Zorg ervoor dat je invoergegevens een kolom Cell Location bevatten met JSON-gegevens voor breedte- en lengtegraad.

Ensure you have an active OpenCage API key with sufficient requests available for your data volume.

Zorg ervoor dat je een actieve OpenCage API-sleutel hebt met voldoende verzoeken beschikbaar voor je datavolume.


---


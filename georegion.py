import pandas as pd
import json
import os
from opencage.geocoder import OpenCageGeocode

# OpenCage API anahtarınızı buraya yazın
API_KEY = 'YOUR_OPENCAGE_API_KEY'
geocoder = OpenCageGeocode(API_KEY)

# Excel dosyasını yükleyin
data = pd.read_excel("your_excel_file.xlsx")  # Dosya adını burada güncelleyin

# 'Country', 'Region' ve 'County/City' sütunlarını ekleyin ve boş bırakın
data['Country'] = None
data['Region'] = None
data['County/City'] = None

# Ülke, il ve ilçe bilgisi almak için fonksiyon
def get_location_info(lat, lon):
    try:
        result = geocoder.reverse_geocode(lat, lon, language='en')
        if result and 'country' in result[0]['components']:
            country = result[0]['components']['country']
            region = result[0]['components'].get('state', None)  # İl bilgisi
            county_city = result[0]['components'].get('county', None) or result[0]['components'].get('city', None)  # İlçe bilgisi
            return country, region, county_city
    except Exception as e:
        print(f"Hata: {e}")
    return None, None, None

# Veriyi işleyin
for index, row in data.iterrows():
    cell_location = row['Cell Location']
    
    # 'Cell Location' hücresinin boş olup olmadığını kontrol edin
    if pd.notna(cell_location):
        try:
            # JSON formatını çözümle
            location_data = json.loads(cell_location)
            lat = location_data["Lat"]
            lon = location_data["Lon"]
            
            # Ülke, il ve ilçeyi al ve ilgili sütunlara yaz
            country, region, county_city = get_location_info(lat, lon)
            data.at[index, 'Country'] = country
            data.at[index, 'Region'] = region
            data.at[index, 'County/City'] = county_city
        except (json.JSONDecodeError, KeyError, TypeError) as e:
            print(f"Satır {index} hata: {e}")

# Yeni dosya adını oluşturun
def generate_unique_filename(filename):
    base, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(new_filename):
        new_filename = f"{base}({counter}){extension}"
        counter += 1
    return new_filename

# Sonucu yeni bir dosyaya kaydedin
output_filename = generate_unique_filename("your_excel_file_with_location_details.xlsx")
data.to_excel(output_filename, index=False)
print(f"Ülke, il ve ilçe bilgileri başarıyla eklendi ve {output_filename} olarak kaydedildi.")

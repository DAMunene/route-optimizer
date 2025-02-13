import googlemaps
import csv
import time
from django.conf import settings

# Replace with your actual Google Maps API key
API_KEY = settings.GOOGLE_MAPS_API_KEY

# Initialize the Google Maps Client
gmaps = googlemaps.Client(key=API_KEY)

# Input and output file paths
input_csv_file = "fuel-prices-for-be-assessment.csv"  # Replace with the actual file name
output_csv_file = "fuel_prices_with_coordinates.csv"

# Function to geocode an address
def geocode_address(address):
    try:
        geocode_result = gmaps.geocode(address)
        if geocode_result:
            location = geocode_result[0]["geometry"]["location"]
            return location["lat"], location["lng"]
    except Exception as e:
        print(f"Error geocoding {address}: {e}")
    return None, None

# Read the CSV and add coordinates
with open(input_csv_file, mode="r", encoding="utf-8") as infile, open(output_csv_file, mode="w", newline="", encoding="utf-8") as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ["latitude", "longitude"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()

    for row in reader:
        full_address = f"{row['Address']}, {row['City']}, {row['State']}, USA"
        lat, lon = geocode_address(full_address)

        # Add lat/lon to the row
        row["latitude"] = lat
        row["longitude"] = lon

        writer.writerow(row)
        print(f"Geocoded: {full_address} -> ({lat}, {lon})")

        time.sleep(1)  # Respect API rate limits

print(f"Geocoding completed! Updated data saved to {output_csv_file}")

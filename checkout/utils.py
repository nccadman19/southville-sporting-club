from geopy.geocoders import Nominatim
import requests

# Create a Geolocator instance (requires internet connection)
geolocator = Nominatim(user_agent="bag")

def determine_country_from_postcode(postcode):
    try:
        location = geolocator.geocode(postcode)
        if location:
            # Extract country code (e.g., 'GB' for United Kingdom)
            country_code = location.raw.get("address", {}).get("country_code")
            return country_code
    except Exception as e:
        pass
    return None

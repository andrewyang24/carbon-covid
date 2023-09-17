import requests
from .custom_exceptions import CarbonIntensityAPIError

class CarbonIntensityController:
    @staticmethod
    def get_carbon_intensity(region, date):
        # Mapping of region names to numeric IDs
        region_mapping = {
            'North Scotland': 1,
            'South Scotland': 2,
            'North West England': 3,
            'North East England': 4,
            'Yorkshire': 5,
            'North Wales': 6,
            'South Wales': 7,
            'West Midlands': 8,
            'East Midlands': 9,
            'East England': 10,
            'South West England': 11,
            'South England': 12,
            'London': 13,
            'South East England': 14,
            'England': 15,
            'Scotland': 16,
            'Wales': 17,
        }

        # Check if the provided region is a valid region name
        if region in region_mapping:
            
            region_id = region_mapping[region]
            base_url = "https://api.carbonintensity.org.uk"
            endpoint = f"/regional/intensity/{date}/fw24h/regionid/{region_id}"

            # Make the API request
            try:
                response = requests.get(f"{base_url}{endpoint}")
                # Check if the request was successful (status code 200)
                if response.status_code == 200:
                    data = response.json()
                    return data
                else:
                    # Handle API error responses
                    error_message = f"Carbon Intensity API error: {response.status_code} - {response.text}"
                    raise CarbonIntensityAPIError(error_message)

            except requests.exceptions.RequestException as e:
                # Handle connection or request errors
                error_message = (f"Request error: {e}")
                raise CarbonIntensityAPIError(error_message)
        else:
            # Invalid region name provided
            raise CarbonIntensityAPIError("Invalid region name provided")

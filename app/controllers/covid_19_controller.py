import requests
from .custom_exceptions import Covid19APIError

class Covid19Controller:
    @staticmethod
    def get_covid_19(region, date):
        # Mapping of region names to numeric IDs
        region_mapping = {
            'North Scotland': "S92000003",
            'South Scotland': "S92000003",
            'North West England': "E12000002",
            'North East England': "E12000001",
            'Yorkshire': "E12000003",
            'North Wales': "W92000004",
            'South Wales': "W92000004",
            'West Midlands': "E12000005",
            'East Midlands': "E12000004",
            'East England': "E12000006",
            'South West England': "E12000009",
            'South England': "E12000008",
            'London': "E12000007",
            'South East England': "E12000008",
            'England': "E92000001",
            'Scotland': "S92000003",
            'Wales': "W92000004",
        }

        # Check if the provided region is a valid region name
        if region in region_mapping:

            area_code = region_mapping[region]
            base_url = "https://api.coronavirus.data.gov.uk/generic"
            area_type = "region"
            metric = "newCasesBySpecimenDate"
            endpoint = f"/soa/{area_type}/{area_code}/{metric}?date={date}"

            # Make the API request
            try:
                response = requests.get(f"{base_url}{endpoint}")
                # Check if the request was successful (status code 200)
                if response.status_code == 200:
                    data = response.json()
                    return data
                elif response.status_code == 204:
                    # Handle undocumented responses
                    error_message = f"Covid 19 API error: {response.status_code} - Undocumented. Likely that the data doesn't exist for the selected area type and metric combination"
                    raise Covid19APIError(error_message)
                else:
                    # Handle other API error responses
                    error_message = f"Covid 19 API error: {response.status_code} - {response.text}"
                    raise Covid19APIError(error_message)

            except requests.exceptions.RequestException as e:
                # Handle connection or request errors
                error_message = (f"Request error: {e}")
                raise Covid19APIError(error_message)
        else:
            # Invalid region name provided
            raise Covid19APIError("Invalid region name provided")

from flask import Flask, request, jsonify, render_template
from app.controllers.carbon_intensity_controller import CarbonIntensityAPIError
from app.controllers.covid_19_controller import Covid19APIError
import firebase_admin
from firebase_admin import credentials
from app.controllers.firebase_cache import fetch_carbon_intensity, fetch_covid_19

# Initialize Firebase Admin SDK with credentials
cred = credentials.Certificate('c:\\Users\\andre\\Desktop\\My Comp Sci Projects\\api-keys\\carbon-covid-firebase-adminsdk-cixd3-a21d142d93.json')
firebase_admin.initialize_app(cred)

app = Flask(__name__, template_folder='../../interface/templates', static_folder='../../interface/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/api/combined_data", methods=["GET"])
def get_combined_data():
    region = request.args.get("region")
    date = request.args.get("date")

    # Check if the provided region is valid
    valid_regions = {
        'North Scotland', 'South Scotland', 'North West England', 'North East England',
        'Yorkshire', 'North Wales', 'South Wales', 'West Midlands', 'East Midlands',
        'East England', 'South West England', 'South England', 'London', 'South East England',
        'England', 'Scotland', 'Wales',
    }
    if region not in valid_regions:
        return jsonify({"error": "Invalid region name"}), 400  # Return a 400 Bad Request

    try:
        carbon_intensity_data = fetch_carbon_intensity(region, date)
        covid_19_data = fetch_covid_19(region, date)

        if carbon_intensity_data and covid_19_data:
            return jsonify({
                "carbon_intensity": carbon_intensity_data,
                "covid_19": covid_19_data
            })
        else:
            return jsonify({"error": "Data not found"}), 404
    except CarbonIntensityAPIError as carbon_intensity_error:
        return jsonify({"error": str(carbon_intensity_error)}), 500  # Internal Server Error
    except Covid19APIError as covid_19_error:
        return jsonify({"error": str(covid_19_error)}), 500  # Internal Server Error

if __name__ == "__main__":
    app.run(debug=True)

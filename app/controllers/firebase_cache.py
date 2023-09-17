from firebase_admin import credentials, firestore
from app.controllers.carbon_intensity_controller import CarbonIntensityController
from app.controllers.covid_19_controller import Covid19Controller

def fetch_carbon_intensity(region, date):
    db = firestore.client()
    cache_key = f"{region}_{date}"
    doc_ref = db.collection('carbon_intensity_cache').document(cache_key)

    # Attempt to retrieve data from Firestore
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        # If data is not in cache, fetch it from the API
        carbon_intensity_data = CarbonIntensityController.get_carbon_intensity(region, date)

        if carbon_intensity_data:
            # Cache the data in Firestore with the combined key
            db.collection('carbon_intensity_cache').document(cache_key).set(carbon_intensity_data)
            return carbon_intensity_data

        return None

def fetch_covid_19(region, date):
    db = firestore.client()
    cache_key = f"{region}_{date}"
    doc_ref = db.collection('covid_19_cache').document(cache_key)

    # Attempt to retrieve data from Firestore
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        # If data is not in cache, fetch it from the API
        covid_19_data = Covid19Controller.get_covid_19(region, date)

        if covid_19_data:
                # Cache the data in Firestore with the combined key
                db.collection('covid_19_cache').document(cache_key).set(covid_19_data)
                return covid_19_data

        return None

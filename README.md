# Carbon and COVID-19 API

This API combines data from the Carbon Intensity and COVID-19 APIs for a given region and date.

## How to Run

1. Install the required packages using `pip install -r requirements.txt`.
2. Run the API using `python run.py`.

## API Endpoints

- `/api/combined_data`: Get combined Carbon Intensity and COVID-19 data for a given region and date.

## Usage

Example request:

```http
GET /api/combined_data?region=London&date=2023-09-01

import requests
import pandas as pd

# Make the HTTP request
response = requests.get('https://api.data.gov.my/weather/forecast/')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()

    # Create a list to hold the data
    records = []

    # Process each item in the JSON data
    for item in data:
        record = {
            'Location': item['location']['location_name'],
            'Date': item['date'],
            'Morning Forecast': item['morning_forecast'],
            'Afternoon Forecast': item['afternoon_forecast'],
            'Night Forecast': item['night_forecast'],
            'Summary Forecast': item['summary_forecast'],
            'Summary When': item['summary_when'],
            'Min Temperature (°C)': item['min_temp'],
            'Max Temperature (°C)': item['max_temp']
        }
        records.append(record)

    # Create a DataFrame from the list of records
    df = pd.DataFrame(records)
    forecast_mapping = {
    'Berjerebu': 0.1,  # Hazy
    'Tiada hujan': 0.2,  # No rain
    'Hujan': 0.3,  # Rain
    'Hujan di beberapa tempat': 0.4,  # Scattered rain
    'Hujan di satu dua tempat': 0.5,  # Isolated rain
    'Hujan di satu dua tempat di kawasan pantai': 0.5,  # Isolated rain over coastal areas
    'Hujan di satu dua tempat di kawasan pedalaman': 0.5,  # Isolated rain over inland areas
    'Ribut petir': 0.6,  # Thunderstorms
    'Ribut petir di beberapa tempat': 0.7,  # Scattered thunderstorms
    'Ribut petir di beberapa tempat di kawasan pedalaman': 0.7,  # Scattered thunderstorms over inland areas
    'Ribut petir di satu dua tempat': 0.8,  # Isolated thunderstorms
    'Ribut petir di satu dua tempat di kawasan pantai': 0.8,  # Isolated thunderstorms over coastal areas
    'Ribut petir di satu dua tempat di kawasan pedalaman': 0.8  # Isolated thunderstorms over inland areas
    }

    df['Energy Output'] = df['Max Temperature (°C)'] * 0.5 + df['Morning Forecast'].map(forecast_mapping) * 100

    # Save the DataFrame to a CSV file
    df.to_csv('weather_forecast1.csv', index=False)

    print("Data has been saved to 'weather_forecast.csv'")
else:
    print(f"Error: Unable to fetch data. Status code: {response.status_code}")

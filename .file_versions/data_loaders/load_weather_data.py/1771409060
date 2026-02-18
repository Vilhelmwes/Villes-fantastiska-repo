import pandas as pd
import requests

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Load weather data from Open Meteo API (no API key needed).
    """
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=52.52&longitude=13.41"
        "&hourly=temperature_2m,windspeed_10m"
        "&forecast_days=7"
    )

    response = requests.get(url)
    response.raise_for_status()
    
    data = response.json()
    
    # Flatten the nested JSON into a DataFrame
    df = pd.DataFrame({
        'time': data['hourly']['time'],
        'temperature_c': data['hourly']['temperature_2m'],
        'windspeed_kmh': data['hourly']['windspeed_10m']
    })
    
    df['time'] = pd.to_datetime(df['time'])
    
    return df
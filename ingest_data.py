import pandas as pd
import requests
from sqlalchemy import create_engine

def fetch_weather_data():
    url = "https://api.open-meteo.com/v1/forecast?latitude=59.3294&longitude=18.0687&hourly=temperature_2m,snowfall&timezone=Europe%2FBerlin&start_date=2026-01-01&end_date=2026-02-20"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()

    df = pd.DataFrame({
        'time': data['hourly']['time'],
        'temperature_c': data['hourly']['temperature_2m'],
        'snowfall':data['hourly']['snowfall']
    })
    df['time'] = pd.to_datetime(df['time'])
    return df

def load_to_postgres(df):
    engine = create_engine("postgresql://postgres:postgres@localhost:5432/mydb")
    df.to_sql(name='weather_history_2026', con=engine, schema='public', if_exists='replace', index=False)

def main():
    df = fetch_weather_data()
    load_to_postgres(df)

if __name__ == "__main__":
    main()
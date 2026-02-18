import pandas as pd
import requests
from sqlalchemy import create_engine

def fetch_weather_data():
    """
    Fetch weather data from Open Meteo API (no API key needed).
    """
    print("Fetching weather data from API...")
    
    url = (
        "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&models=dmi_seamless"
    )
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Only use fields that exist in the response
        df = pd.DataFrame({
            'time': data['hourly']['time'],
            'temperature_c': data['hourly']['temperature_2m']
        })

        df['time'] = pd.to_datetime(df['time'])

        print(f"✓ Fetched {len(df)} rows of weather data")
        return df

    except requests.exceptions.RequestException as e:
        print(f"✗ Error fetching data: {e}")
        return None

def load_to_postgres(df):
    """
    Load DataFrame to Postgres database.
    """
    if df is None:
        print("✗ No data to load")
        return
    
    print("Connecting to Postgres...")
    
    # Connection string
    connection_string = "postgresql://postgres:postgres@localhost:5432/mydb"
    
    try:
        engine = create_engine(connection_string)
        
        # Write to database
        df.to_sql(
            name='weather_forecast',
            con=engine,
            schema='public',
            if_exists='replace',  # 'replace' or 'append'
            index=False
        )
        
        print(f"✓ Successfully loaded {len(df)} rows to table 'weather_forecast'")
        
    except Exception as e:
        print(f"✗ Error loading to Postgres: {e}")

def main():
    print("=== Weather Data Pipeline ===\n")
    
    # Step 1: Fetch data from API
    df = fetch_weather_data()
    
    if df is not None:
        # Step 2: Preview data
        print("\nData preview:")
        print(df.head())
        
        # Step 3: Load to Postgres
        print()
        load_to_postgres(df)
    
    print("\n=== Pipeline Complete ===")

if __name__ == "__main__":
    main()
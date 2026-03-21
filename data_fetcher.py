import requests
import pandas as pd
from datetime import datetime
import os

API_KEY = 'your_api_key_here'  # 请替换为您的ExchangeRate-API密钥
BASE_URL = 'https://api.exchangerate-api.com/v4/latest/USD'
DATA_FILE = 'data.csv'

def fetch_exchange_rate():
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        data = response.json()
        rate = data['rates']['CNY']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return timestamp, rate
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None, None

def save_to_csv(timestamp, rate):
    df = pd.DataFrame({'timestamp': [timestamp], 'rate': [rate]})
    if os.path.exists(DATA_FILE):
        df.to_csv(DATA_FILE, mode='a', header=False, index=False)
    else:
        df.to_csv(DATA_FILE, index=False)

def fetch_and_save():
    timestamp, rate = fetch_exchange_rate()
    if timestamp and rate:
        save_to_csv(timestamp, rate)
        print(f"Data saved: {timestamp}, {rate}")
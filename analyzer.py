import pandas as pd

DATA_FILE = 'data.csv'

def load_data():
    try:
        df = pd.read_csv(DATA_FILE)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        return df
    except FileNotFoundError:
        print("Data file not found.")
        return pd.DataFrame()

def calculate_moving_average(window=7):
    df = load_data()
    if df.empty:
        return df
    df['moving_avg'] = df['rate'].rolling(window=window).mean()
    return df
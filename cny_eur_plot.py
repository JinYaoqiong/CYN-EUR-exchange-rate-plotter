import requests
import pandas as pd
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

# ECB API URL for historical exchange rates
API_URL = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.xml'

def fetch_exchange_rates():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.content
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def parse_xml_to_dataframe(xml_data):
    root = ET.fromstring(xml_data)
    data = []
    for cube in root.findall('.//{http://www.ecb.int/vocabulary/2002-08-01/eurofxref}Cube[@time]'):
        date = cube.get('time')
        for rate in cube:
            currency = rate.get('currency')
            if currency == 'CNY':
                value = float(rate.get('rate'))
                data.append({'date': date, 'rate': value})
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    return df

def get_last_7_days_data():
    xml_data = fetch_exchange_rates()
    if xml_data:
        df = parse_xml_to_dataframe(xml_data)
        # Get last 7 days
        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)
        df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
        return df
    return pd.DataFrame()

def plot_exchange_rate_trend(df):
    if df.empty:
        print("No data to plot.")
        return

    sns.set_theme(
        context='paper',
        style='ticks',
        palette='colorblind',
        rc={
            'figure.dpi': 120,
            'savefig.dpi': 300,
            'axes.linewidth': 1.0,
            'lines.linewidth': 2.0,
            'lines.markersize': 6,
            'grid.linewidth': 0.6,
            'grid.alpha': 0.3,
            'font.sans-serif': ['Microsoft YaHei', 'SimHei', 'Noto Sans CJK SC', 'Arial Unicode MS', 'DejaVu Sans'],
            'axes.unicode_minus': False
        }
    )

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(
        data=df,
        x='date',
        y='rate',
        marker='o',
        errorbar=None,
        label='CNY/EUR Exchange Rate',
        ax=ax
    )
    ax.set_xlabel('日期 Date')
    ax.set_ylabel('汇率 Rate (CNY per EUR)')
    ax.set_title('人民币兑欧元汇率走势（近7日）\nCNY/EUR Exchange Rate Trend (Last 7 Days)')
    ax.legend(frameon=False)
    ax.grid(True, axis='y')
    sns.despine(ax=ax)

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax.xaxis.set_major_locator(mdates.DayLocator())
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('cny_eur_trend.png')
    plt.show()  # For display, but in server use savefig
    print("Chart saved as cny_eur_trend.png")

if __name__ == '__main__':
    df = get_last_7_days_data()
    print(df)
    plot_exchange_rate_trend(df)
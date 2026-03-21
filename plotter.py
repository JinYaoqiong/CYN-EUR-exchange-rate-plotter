import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from analyzer import calculate_moving_average

def plot_exchange_rate():
    df = calculate_moving_average()
    if df.empty:
        print("No data to plot.")
        return

    plt.figure(figsize=(10, 5))
    plt.plot(df['timestamp'], df['rate'], label='Exchange Rate (USD/CNY)')
    if 'moving_avg' in df.columns:
        plt.plot(df['timestamp'], df['moving_avg'], label='7-Day Moving Average', linestyle='--')
    plt.xlabel('Time')
    plt.ylabel('Rate')
    plt.title('USD/CNY Exchange Rate Trend')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    print("Saving chart...")
    plt.savefig('exchange_rate_chart.png')
    plt.close()
    print("Chart saved as exchange_rate_chart.png")
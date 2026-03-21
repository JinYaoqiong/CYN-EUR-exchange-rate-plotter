from flask import Flask, render_template_string
import schedule
import time
from data_fetcher import fetch_and_save
from plotter import plot_exchange_rate

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Exchange Rate Trend</title>
</head>
<body>
    <h1>USD/CNY Exchange Rate Trend</h1>
    <img src="/chart" alt="Exchange Rate Chart">
</body>
</html>
"""

@app.route('/')
def index():
    plot_exchange_rate()
    return render_template_string(HTML_TEMPLATE)

@app.route('/chart')
def chart():
    plot_exchange_rate()
    return app.send_static_file('exchange_rate_chart.png')

def run_scheduler():
    schedule.every(5).minutes.do(fetch_and_save)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    # 启动调度器在后台
    import threading
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.daemon = True
    scheduler_thread.start()
    # 启动Flask app
    app.run(debug=True)
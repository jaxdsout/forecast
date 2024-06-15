import os
from dotenv import load_dotenv
import requests

load_dotenv()
key = os.getenv("API_KEY")


def get_data(location, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    # 8 DATA POINTS A DAY FROM API
    filtered_data = filtered_data[:8 * forecast_days]
    return filtered_data


if __name__ == '__main__':
    print(get_data(location="Tokyo", forecast_days=3))
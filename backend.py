import os
import requests

API_KEY = os.getenv("WEATHER_API_KEY")


def get_data(place="Galle", days=1):
    try:
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
        response = requests.get(url)
        data = response.json()

        # filtering data on number of days
        filtered_data = data['list']
        num_days = 8 * days
        filtered_data = filtered_data[:num_days]

        return filtered_data
    except KeyError:
        return


if __name__ == "__main__":
    print(get_data("Galle", 3))
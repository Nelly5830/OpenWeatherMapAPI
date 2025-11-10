from abc_api_base import APIBase
import os
from dotenv import load_dotenv

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

class APIWeather(APIBase):
    def __init__(self, city, units='imperial', timeout=10):
        load_dotenv()
        api_key = os.getenv('OWM_API_KEY')

        params = {
            'q': city,
            'appid': api_key,
            'units': units
        }

        super().__init__(BASE_URL, params, timeout)
        self.__data = None

    def call_api(self):
        self.__data = self.get_api()
        if self.__data is None:
            return self.status, self.message
        return self.status, 'Success'

    def __str__(self):
        if not self.__data:
            return '\nNo data available to display.\n'

        data = self.__data
        name = data.get('name', 'Unknown location')
        country = data.get('sys', {}).get('country', '')
        temp = data.get('main', {}).get('temp', 'N/A')
        humidity = data.get('main', {}).get('humidity', 'N/A')
        wind = data.get('wind', {}).get('speed', 'N/A')
        weather_desc = data.get('weather', [{}])[0].get('description', 'No description')

        sunrise = data.get('sys', {}).get('sunrise', 0)
        sunset = data.get('sys', {}).get('sunset', 0)
        from datetime import datetime
        sunrise_time = datetime.fromtimestamp(sunrise).strftime('%H:%M:%S') if sunrise else 'N/A'
        sunset_time = datetime.fromtimestamp(sunset).strftime('%H:%M:%S') if sunset else 'N/A'

        return (
            f"\nWeather for {name}, {country}:\n"
            f"  Description: {weather_desc.capitalize()}\n"
            f"  Temperature: {temp}°\n"
            f"  Humidity: {humidity}%\n"
            f"  Wind Speed: {wind} mph\n"
            f"  Sunrise: {sunrise_time}\n"
            f"  Sunset: {sunset_time}\n"
        )

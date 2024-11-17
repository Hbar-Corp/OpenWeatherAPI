import os
import requests
from constant import *
from dotenv import load_dotenv


class WeatherRequester:
    load_dotenv()

    def __init__(self):
        self._api_key = os.getenv("API_KEY")

    def get_weather_by_location(self, latitude: float, longitude: float, units: str = "celcius", lang: str = "fr") -> dict:
        """
        Methode permettant d'obtenir la méteo actuelle par localisation geographique(latitude, longitude).
        :param latitude: Latitude de l'emplacement géographique [-90; 90]
        :param longitude: Longitude de l'emplacement géographique [-180; 180]
        :param units: Unité de mesure de la températude. Unités disponibles: celcius (défaut), fahrenheit, kelvin
        :param lang: Language des données requêtées (Français par défaut)
        :return:
        """
        url = end_point + f"weather?lat={latitude}&lon={longitude}&lang={lang}&appid={self._api_key}&units={UNITS[units]}"
        response = requests.get(url=url)
        return response.json()

    def get_weather_by_city_name(self, city_name: str, units: str = "celcius", lang: str = "fr") -> dict:
        """

        :param city_name:
        :param units:
        :param lang:
        :return:
        """
        url = end_point + f"weather?q={city_name}&lang={lang}&appid={self._api_key}&units={UNITS[units]}"
        response = requests.get(url=url)
        return response.json()

    def get_weather_forcast_by_location(self, latitude: float, longitude: float, units: str = "celcius", lang: str = "fr") -> dict:
        """

        :param latitude:
        :param longitude:
        :param units:
        :param lang:
        :return:
        """
        url = end_point + f"forecast?lat={latitude}&lon={longitude}&lang={lang}&appid={self._api_key}&units={UNITS[units]}"
        response = requests.get(url=url)
        return response.json()

    def get_weather_forcast_by_city_name(self, city_name: str, units: str = "celcius", lang: str = "fr") -> dict:
        """

        :param city_name:
        :param units:
        :param lang:
        :return:
        """
        url = end_point + f"forecast?q={city_name}&lang={lang}&appid={self._api_key}&units={UNITS[units]}"
        response = requests.get(url=url)
        return response.json()

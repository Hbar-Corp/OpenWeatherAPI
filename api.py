import os

import pandas as pd
import requests
import weather_parser as parser
from constant import end_point, UNITS
from dotenv import load_dotenv


class WeatherRequester:
    load_dotenv()

    def __init__(self):
        self._api_key = os.getenv("API_KEY")

    def get_weather_by_location(self, latitude: float, longitude: float, units: str = "celcius", lang: str = "fr") -> dict:
        """
        Methode permettant d'obtenir la méteo actuelle par localisation geographique (latitude, longitude).
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
        Methode permettant d'obtenir la météo actuelle par nom de ville.
        :param city_name: Nom de ville (e.g. Paris)
        :param units: Unité de mesure de la températude. Unités disponibles: celcius (défaut), fahrenheit, kelvin
        :param lang: Language des données requêtées (Français par défaut)
        :return:
        """
        url = end_point + f"weather?q={city_name}&lang={lang}&appid={self._api_key}&units={UNITS[units]}"
        response = requests.get(url=url)
        return response.json()

    def get_weather_forcast_by_location(self, latitude: float, longitude: float, units: str = "celcius", lang: str = "fr") -> dict:
        """
        Methode permettant d'obtenir une prévision météo sur cinq jours par localisation geographique (latitude, longitude).
        :param latitude: Latitude de l'emplacement géographique [-90; 90]
        :param longitude: Longitude de l'emplacement géographique [-180; 180]
        :param units: Unité de mesure de la températude. Unités disponibles: celcius (défaut), fahrenheit, kelvin
        :param lang: Language des données requêtées (Français par défaut)
        :return:
        """
        url = end_point + f"forecast?lat={latitude}&lon={longitude}&lang={lang}&appid={self._api_key}&units={UNITS[units]}"
        response = requests.get(url=url)
        return response.json()

    def get_weather_forcast_by_city_name(self, city_name: str, units: str = "celcius", lang: str = "fr", parse=True) -> pd.DataFrame:
        """
        Methode permettant d'obtenir une prévision météo sur cinq jours par nom de ville.
        :param city_name: Nom de ville (e.g. Paris)
        :param units: Unité de mesure de la températude. Unités disponibles: celcius (défaut), fahrenheit, kelvin
        :param lang: Language des données requêtées (Français par défaut)
        :return:
        """
        url = end_point + f"forecast?q={city_name}&lang={lang}&appid={self._api_key}&units={UNITS[units]}"
        response = requests.get(url=url)
        json_data = response.json()
        if parse:
            _df = parser.parse_weather_forcast(json_data)
            return _df
        else:
            return json_data

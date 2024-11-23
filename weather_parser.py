import pandas as pd


def parse_weather_forcast(json_data: dict) -> pd.DataFrame:
    """
    Mise en forme dans une DataFrame des données reçu suivant la reception des données de l'api OpenWeather.
    :param json_data: Dictionnaire contenant les données receptionnés suivant la GET request de l'api OpenWeather.
    :return:
    """
    _df = pd.DataFrame(data="", columns=["Datetime", "Temp", "Temp max", "Temp min", "Humidité", "Pression", "Description", "Icon ID"],
                       index=[i for i in range(int(json_data["cnt"]))])

    for i, day in enumerate(json_data["list"]):
        _df.loc[i, "Datetime"] = day["dt_txt"]
        _df.loc[i, "Temp"] = int(day["main"]["temp"])
        _df.loc[i, "Temp max"] = int(day["main"]["temp_max"])
        _df.loc[i, "Temp min"] = int(day["main"]["temp_min"])
        _df.loc[i, "Humidité"] = float(day["main"]["humidity"])
        _df.loc[i, "Pression"] = float(day["main"]["pressure"])
        _df.loc[i, "Description"] = day["weather"][0]["description"].capitalize()
        _df.loc[i, "Icon ID"] = day["weather"][0]["id"]

    _df["Datetime"] = pd.to_datetime(_df.Datetime)
    return _df

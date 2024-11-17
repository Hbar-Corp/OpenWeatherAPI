import datetime
import pandas as pd


def parse_weather_forcast(json_data) -> pd.DataFrame:
    """

    :param json_data:
    :return:
    """
    _df = pd.DataFrame(data="", columns=["Datetime", "Temp", "Temp max", "Temp min", "Humidité", "Pression", "Description"],
                       index=[i for i in range(int(json_data["cnt"]))])

    for i, day in enumerate(json_data["list"]):
        _df.loc[i, "Datetime"] = day["dt_txt"]
        _df.loc[i, "Temp"] = float(day["main"]["temp"])
        _df.loc[i, "Temp max"] = float(day["main"]["temp_max"])
        _df.loc[i, "Temp min"] = float(day["main"]["temp_min"])
        _df.loc[i, "Humidité"] = float(day["main"]["humidity"])
        _df.loc[i, "Pression"] = float(day["main"]["pressure"])
        _df.loc[i, "Description"] = day["weather"][0]["description"].capitalize()

    _df["Datetime"] = pd.to_datetime(_df.Datetime)
    return _df

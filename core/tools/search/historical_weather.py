import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry

WMO_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Drizzle, light",
    53: "Drizzle, moderate",
    55: "Drizzle, dense intensity",
    56: "Freezing drizzle, light",
    57: "Freezing drizzle, heavy",
    61: "Rain, slight",
    63: "Rain, moderate",
    65: "Rain, heavy",
    66: "Freezing rain, slight",
    67: "Freezing rain, heavy",
    71: "Snow fall, slight",
    73: "Snow fall, moderate",
    75: "Snow fall, heavy",
    77: "Snow grains",
    80: "Rain showers, slight",
    81: "Rain showers, moderate",
    82: "Rain showers, violent",
    85: "Snow showers, slight",
    86: "Snow showers, heavy",
    95: "Thunderstorm, slight",
    96: "Thunderstorm, moderate",
    99: "Thunderstorm, heavy"
}


def historical_weather(
        longitude: float,
        latitude: float,
        start_date: str,
        end_date: str,
) -> pd.DataFrame:
    """
    This function searches the historical weather from openmeteo API.

    Parameters
    ----------
    :param start_date:
    The start date of the historical weather in the format of "YYYY-MM-DD".
    :param end_date:
    The end date of the historical weather in the format of "YYYY-MM-DD".
    :param longitude:
    :param latitude:


    Returns
    -------
    pd.dataframe
        The information of the historical weather.

    """

    # Set up the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after=-1)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min"],
        "timezone": "auto"
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]
    print(f"Coordinates {response.Latitude()}°E {response.Longitude()}°N")
    print(f"Elevation {response.Elevation()} m asl")
    print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
    print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

    # Process daily data. The order of variables needs to be the same as requested.
    daily = response.Daily()
    daily_weather_code = daily.Variables(0).ValuesAsNumpy()
    daily_weather_condition = [WMO_CODES[int(code)] for code in daily_weather_code]
    daily_temperature_2m_max = daily.Variables(1).ValuesAsNumpy()
    daily_temperature_2m_min = daily.Variables(2).ValuesAsNumpy()

    daily_data = {"date": pd.date_range(
        start=pd.to_datetime(daily.Time(), unit="s"),
        end=pd.to_datetime(daily.TimeEnd(), unit="s"),
        freq=pd.Timedelta(seconds=daily.Interval()),
        inclusive="left"
    ), "weather": daily_weather_condition, "temperature_2m_max": daily_temperature_2m_max,
        "temperature_2m_min": daily_temperature_2m_min}

    daily_dataframe = pd.DataFrame(data=daily_data)
    # print(daily_dataframe)
    return daily_dataframe

# historical_weather(116.481488,39.990464,"2021-01-01","2021-01-02")

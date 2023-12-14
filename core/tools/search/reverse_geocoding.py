import os

import requests
import json


def reverse_geocoding(
        longitude: float,
        latitude: float
) -> str:
    """
    This function transforms the geo coordinates(longitude and latitude) to POIs (mainland China).
    The POI correspond to the information of the location.
    The usage of this tool is strictly limited.
    Please limit your usage to avoid exceeding the limit.(use geo_decode instead)

    Parameters
    ----------
    longitude : str
        Longitude of the location
    latitude  : str
        Latitude of the location

    Returns
    -------
    str

    """
    url = "https://restapi.amap.com/v3/geocode/regeo?parameters"

    params = {
        "location": str(longitude)+","+str(latitude),
        "key": os.environ["GAO_DE_API_KEY"],
    }

    response = requests.get(url, params=params)
    response = json.loads(response.text)["regeocode"]
    print(response)
    return str(response)


if __name__ == '__main__':
    reverse_geocoding(116.481488,39.990464)

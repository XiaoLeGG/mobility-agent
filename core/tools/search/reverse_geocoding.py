import requests
import json


def reverse_geocoding(
        longitude: float,
        latitude: float
) -> str:
    """
    This function transforms the geo coordinates(longitude and latitude) to POIs (mainland China).
    The POI correspond to the information of the location.

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
        "key": "2a2b92d607ebc4b19abcb32353bb5d81"
    }

    response = requests.get(url, params=params)
    response = json.loads(response.text)["regeocode"]
    print(response)
    return str(response)


if __name__ == '__main__':
    reverse_geocoding(116.481488,39.990464)

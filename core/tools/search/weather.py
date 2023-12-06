import requests
import json


def weather(
        citycode: str
) -> str:
    """
    This function searches the current weather from GaoDe MAP(mainland China) API.

    Parameters
    ----------
    citycode : str
        The city code of the city.(adcode)

    Returns
    -------
    str
        The information of the current weather(a json string).
    """
    url = "https://restapi.amap.com/v3/weather/weatherInfo?parameters"

    params = {
        "city": citycode,
        "key": "2a2b92d607ebc4b19abcb32353bb5d81"
    }

    response = requests.get(url, params=params)
    response = json.loads(response.text)["lives"][0]
    return str(response)


if __name__ == '__main__':
    weather("110101")

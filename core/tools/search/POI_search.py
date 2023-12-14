import os

import requests
import json


def POI_search(
        keywords: str,
        city: str
) -> str:
    """
    This function searches the specific POI from GaoDe MAP(mainland China) API.
    The POI correspond to the information of the location.

    Parameters
    ----------
    keywords : str
        The keywords(name) of the POI.
    city : str
        The city where the POI is located.

    Returns
    -------
    str
        The information of the POI(a json string).
    """
    url = "https://restapi.amap.com/v3/place/text?parameters"

    params = {
        "keywords": keywords,
        "city": city,
        "key": os.environ["GAO_DE_API_KEY"],
        "page": 1,
        "offset": 10
    }

    response = requests.get(url, params=params)
    try:
        response = json.loads(response.text)
        retrieved_pois = [
            {key: poi[key] for key in ("name", "type", "adname", "address", "location") if key in poi}
            for poi in response["pois"]
        ]
        print(retrieved_pois)
        return str(retrieved_pois)
    except Exception:
        return "[]"


if __name__ == '__main__':
    POI_search("北京大学", "北京")

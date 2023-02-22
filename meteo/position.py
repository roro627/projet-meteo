from typing import Tuple

import requests


def get_lat_lon_from_ip() -> Tuple[float, float]:
    lres = requests.get("http://ip-api.com/json/?fields=lat,lon")
    rd = lres.json()
    return rd["lat"], rd["lon"]

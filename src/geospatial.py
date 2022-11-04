import json
from typing import Tuple

import requests


def prepare_address(address: str) -> str:
    return address.replace(" ", "%20")


def address_to_coordinates(address: str) -> Tuple[str | float, float]:
    address = prepare_address(address)
    url = "http://api.positionstack.com/v1/forward" \
          "?access_key=cab89e3651ff9164ebd06a174026b011" \
          f"&query='{address}'"
    response = requests.get(url)
    if response.status_code == 200:
        poi = json.loads(response.content)
        latitude = poi["data"][0]["latitude"]
        longitude = poi["data"][0]["longitude"]
        return latitude, longitude

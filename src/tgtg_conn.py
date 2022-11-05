import os
from typing import Dict, List

from tgtg import TgtgClient


class TgtgItem:
    def __init__(self, info: Dict) -> None:
        self.info = info

    @property
    def distance(self) -> float:
        """Distance to the store from the request location"""
        return f"{self.info['distance']:.2f}"

    @property
    def image_url(self) -> str:
        """Url of the item picture"""
        return self.info["item"]["cover_picture"]["current_url"]

    @property
    def name(self) -> str:
        """Name of the item"""
        return self.info["item"]["name"]

    @property
    def price(self) -> float:
        """Price of the item"""
        return self.info["item"]["price_including_taxes"]["minor_units"] / (
                10 ** self.info["item"]["price_including_taxes"]["decimals"])

    @property
    def store(self) -> str:
        """Name of the supplying store"""
        return self.info["store"]["store_name"]

    @property
    def is_available(self) -> bool:
        return self.info.keys()

    def __repr__(self):
        return str([self.name, self.price, self.store, self.distance, self.image_url])


def get_client() -> TgtgClient:
    return TgtgClient(
        access_token=os.environ["TGTG_ACCESS_TOKEN"],
        refresh_token=os.environ["TGTG_REFRESH_TOKEN"],
        user_id=os.environ["TGTG_USER_ID"]
    )


def get_items(client: TgtgClient = get_client(), latitude: float = 52.213036, longitude=21.019615,
              radius: int = 15
              ) -> List[TgtgItem]:
    raw = client.get_items(favorites_only=False, latitude=latitude, longitude=longitude, radius=radius,
                           with_stock_only=True)
    parsed = [TgtgItem(item) for item in raw]
    return parsed

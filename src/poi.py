from typing import Tuple


class POI:
    def __init__(self, config: Tuple) -> None:
        print(config)
        self.id = config[0]
        self.name = config[1]
        self.address = f"{config[4]}, {config[2]} {config[3]}"
        self.latitude = float(config[5])
        self.longitude = float(config[6])
        self.is_full = bool(config[7])
        self.door_open = bool(config[8])
        self.url = config[9]

    def __repr__(self):
        if self.url:
            return f"{self.name}, {self.address} ({self.latitude}, {self.longitude}) ({self.url})"
        return f"{self.name}, {self.address} ({self.latitude}, {self.longitude})"

    def to_marker(self):
        return f"var poi_{self.id} = L.marker([{self.latitude}, {self.longitude}]);" \
               f"poi_{self.id}.addTo(map).bindPopup('<h3>{self.name}</h3>" \
               f"<p class=\"label-address\">{self.address}</p>" \
               f"<a href=\"/poi/{self.id}\">Zobacz więcej informacji</a><br>" \
               f"<a href=\"/admin/{self.id}\">Panel administracyjny</a>');"

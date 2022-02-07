import requests


class Hellcase:
    def __init__(self):
        self.dict = {
            "item_names": [],
            "prices": [],
        }

        offset = 0
        while offset <= 3987:
            r = requests.get(f"https://api.hellcase.com/csgo/en/item?&range_from=40&range_to=2500&per_page=100"
                             f"&stattrak=1 "
                             f"&sort=desc&offset={offset}").json()
            for item in r["items"]:
                if item["steam_market_hash_name"][:7] != "Sticker":
                    self.dict["item_names"].append(item["steam_market_hash_name"])
                    self.dict["prices"].append(float(item["steam_price_en"]))
            offset += 100

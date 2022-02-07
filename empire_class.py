import requests

ENDPOINT = "https://csgoempire.gg/api/v2/trading/items?per_page=200&page=1&auction=yes&price_max_above=999999&sort" \
           "=desc&order=market_value"


class Empire:
    def __init__(self):
        self.response = requests.get(ENDPOINT).json()
        self.dict = {
            "item_name": [],
            "item_current_price": [],
            "url": [],
            "wear": []
        }
        for item in self.response["data"]:
            self.item_wear = item["wear"]
            self.item_name = item["name"]
            self.item_base_price = item["market_value"]
            self.item_highest_bid = item["auction_highest_bid"]
            self.url = item["icon_url"]

            if self.item_highest_bid is not None and self.item_highest_bid >= self.item_base_price:
                self.item_price = self.item_highest_bid
            else:
                self.item_price = self.item_base_price

            if self.item_price > 5000:
                self.dict["item_name"].append(self.item_name)
                self.dict["wear"].append(self.item_wear)
                self.dict["url"].append(self.url)

                if len(str(self.item_price)) == 4:
                    self.item_price = f"{str(self.item_price)[:2]}." + f"{str(self.item_price)[2:]}"
                    self.dict["item_current_price"].append(float(self.item_price))
                elif len(str(self.item_price)) == 5:
                    self.item_price = f"{str(self.item_price)[:3]}." + f"{str(self.item_price)[3:]}"
                    self.dict["item_current_price"].append(float(self.item_price))
                elif len(str(self.item_price)) == 6:
                    self.item_price = f"{str(self.item_price)[:4]}." + f"{str(self.item_price)[4:]}"
                    self.dict["item_current_price"].append(float(self.item_price))

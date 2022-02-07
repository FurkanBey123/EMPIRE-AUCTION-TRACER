import requests


class SteamInventory:
    def __init__(self):

        self.steam_dict = {
            "item_names": [],
            "item_owner": [],
            "item_tradable": [],
            "item_description": []
        }

        response_furkan = requests.get("https://steamcommunity.com/inventory/76561198893128342/730/2?l=english&count=5000").json()
        for item_furkan in response_furkan["descriptions"]:
            item_name = item_furkan["market_hash_name"]
            item_tradable = item_furkan["tradable"]
            item_owner = "Furkan"
            if item_tradable == 0:
                description = "Banlı halde bulunan"
            else:
                description = ""
            self.steam_dict["item_names"].append(item_name)
            self.steam_dict["item_owner"].append(item_owner)
            self.steam_dict["item_tradable"].append(item_tradable)
            self.steam_dict["item_description"].append(description)

        response_ahmet = requests.get("https://steamcommunity.com/inventory/76561198346079540/730/2?l=english&count=5000").json()
        for item_ahmet in response_ahmet["descriptions"]:
            item_name = item_ahmet["market_hash_name"]
            item_tradable = item_ahmet["tradable"]
            item_owner = "Ahmet"
            if item_tradable == 0:
                description = "Banlı halde bulunan"
            else:
                description = ""
            self.steam_dict["item_names"].append(item_name)
            self.steam_dict["item_owner"].append(item_owner)
            self.steam_dict["item_tradable"].append(item_tradable)
            self.steam_dict["item_description"].append(description)

        response_mehmet = requests.get("https://steamcommunity.com/inventory/76561199006970785/730/2?l=english&count=5000").json()

        for item_mehmet in response_mehmet["descriptions"]:
            item_name = item_mehmet["market_hash_name"]
            item_tradable = item_mehmet["tradable"]
            item_owner = "Mehmet"
            if item_tradable == 0:
                description = "Banlı halde bulunan"
            else:
                description = ""
            self.steam_dict["item_names"].append(item_name)
            self.steam_dict["item_owner"].append(item_owner)
            self.steam_dict["item_tradable"].append(item_tradable)
            self.steam_dict["item_description"].append(description)

        print(self.steam_dict)

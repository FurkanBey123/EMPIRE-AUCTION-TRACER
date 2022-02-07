from functions import checker
from hellcase_class import Hellcase
from empire_class import Empire
from steam_class import SteamInventory
import time


steam = SteamInventory()
steam_dict = steam.steam_dict

hellcase = Hellcase()
hellcase_dict = hellcase.dict

counter = 0
while True:
    counter += 1

    if counter == 300:
        my_hellcase = Hellcase()
        hellcase_dict = hellcase.dict
        print("HELLCASE HELLCASE HELLCASE HELLCASE HELLCASE HELLCASE HELLCASE HELLCASE")

        steam_data = SteamInventory()
        steam_dict = steam.steam_dict
        print("STEAM STEAM STEAM STEAM STEAM STEAM STEAM STEAM STEAM STEAM STEAM STEAM")

        counter = 0

    print(f"Counter: {counter}")
    try:
        empire = Empire()
        empire_dict = empire.dict
        checker(empire_dict, hellcase_dict, steam_dict)

    except IndexError:
        print(IndexError)
        time.sleep(1)
        pass
    except ValueError:
        print(ValueError)
        time.sleep(1)
        pass

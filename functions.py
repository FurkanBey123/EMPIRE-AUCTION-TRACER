import requests
SHADOW_TOKEN = ""
CHAT_ID = ""


def checker(empire_dict, hellcase_dict, steam_dict):
    for item in empire_dict["item_name"]:
        print(item)
        if item in hellcase_dict["item_names"]:
            empire_index = empire_dict["item_name"].index(item)
            price = empire_dict["item_current_price"][empire_index]
            empire_id = empire_dict["wear"][empire_index]

            hellcase_index = hellcase_dict["item_names"].index(item)
            hellcase_price = hellcase_dict["prices"][hellcase_index]

            discount = (100 - ((price * 0.61) / hellcase_price * 100)).__round__(2)
            if discount >= 31:
                shadow_data = requests.get("https://api.shadowpay.com/api/v2/user/items?token"
                                           f"={SHADOW_TOKEN}&"
                                           f"steam_market_hash_name={item}").json()
                if len(shadow_data["data"]) == 0:
                    if item not in steam_dict["item_names"]:
                        if empire_checker(item, price, empire_id):
                            url = empire_dict["url"][empire_index]
                            message_sender(item_name=item, discount=discount, item_current_price=price,
                                           item_url=url, extra_caption="")
                        else:
                            url = empire_dict["url"][empire_index]
                            message_sender(item_name=item, discount=discount, item_current_price=price,
                                           item_url=url, extra_caption=" Pazarda daha ucuzu var! ")
                    elif item in steam_dict:
                        steam_index = steam_dict["item_names"].index(item)
                        owner = owner_checker(item, steam_dict)
                        trade_description = steam_dict["item_description"][steam_index]
                        if empire_checker(item, price, empire_id):
                            url = empire_dict["url"][steam_index]
                            message_sender(item_name=item, discount=discount, item_current_price=price,
                                           item_url=url,
                                           extra_caption=f"{trade_description}{owner} Bey' de bulunan ")
                        else:
                            url = empire_dict["url"][empire_index]
                            message_sender(item_name=item, discount=discount, item_current_price=price,
                                           item_url=url,
                                           extra_caption=f"{trade_description}{owner} Bey' de bulunan ve aynı "
                                                         f"zamanda pazarda daha ucuzu bulunan")

                elif len(shadow_data["data"]) == 1:
                    if item in steam_dict["item_names"]:
                        steam_index = steam_dict["item_names"].index(item)
                        tradable = steam_dict["item_tradable"][steam_index]
                        if tradable == 1:
                            owner = owner_checker(item, steam_dict)
                            if empire_checker(item, price, empire_id):
                                url = empire_dict["url"][empire_index]
                                message_sender(item_name=item, discount=discount, item_current_price=price,
                                               item_url=url,
                                               extra_caption=f"{owner} Bey' in tek başına hâlihazırda satışa sunmuş olduğu ")
                            else:
                                url = empire_dict["url"][steam_index]
                                message_sender(item_name=item, discount=discount, item_current_price=price,
                                               item_url=url,
                                               extra_caption=f"{owner} Bey' in tek başına hâlihazırda satışa sunmuş olduğu ve "
                                                             f"pazarda daha ucuzu bulunan ")
                        else:
                            owner = owner_checker(item, steam_dict)
                            trade_description = steam_dict["item_description"][steam_index]
                            if empire_checker(item, price, empire_id):
                                url = empire_dict["url"][empire_index]
                                message_sender(item_name=item, discount=discount, item_current_price=price,
                                               item_url=url,
                                               extra_caption=f"Bu itemde pazarda bizden başka birisi var. Aynı zamanda {owner} Bey' de de "
                                                             f"{trade_description} ")
                            else:
                                url = empire_dict["url"][empire_index]
                                message_sender(item_name=item, discount=discount, item_current_price=price,
                                               item_url=url,
                                               extra_caption=f"Bu itemde pazarda bizden başka birisi var. {owner} Bey' de "
                                                             f"{trade_description} ve ebesinin amı şeklinde pazarda daha ucuzu bulunan ")

                    elif item not in steam_dict["item_names"] and discount >= 33:
                        if empire_checker(item, price, empire_id):
                            url = empire_dict["url"][empire_index]
                            message_sender(item_name=item, discount=discount, item_current_price=price,
                                           item_url=url,
                                           extra_caption=f"Markette sadece 1 kişi tarafından satılan ")
                        else:
                            url = empire_dict["url"][empire_index]
                            message_sender(item_name=item, discount=discount, item_current_price=price,
                                           item_url=url,
                                           extra_caption=f"Markette sadece 1 kişi tarafından satılan ve "
                                                         f"pazarda daha da ucuzu bulunan itemimiz ")
                elif len(shadow_data["data"]) == 2:
                    if item in steam_dict["item_names"]:
                        steam_index = steam_dict["item_names"].index(item)
                        tradable = steam_dict["item_tradable"][steam_index]
                        if tradable == 1:
                            owner = owner_checker(item, steam_dict)
                            if empire_checker(item, price, empire_id):
                                url = empire_dict["url"][empire_index]
                                message_sender(item_name=item, discount=discount, item_current_price=price,
                                               item_url=url,
                                               extra_caption=f"{owner} Bey' in yanında ekstra bir kişi ile satışa sunmuş olduğu ")
                            else:
                                url = empire_dict["url"][empire_index]
                                message_sender(item_name=item, discount=discount, item_current_price=price,
                                               item_url=url,
                                               extra_caption=f"{owner} Bey' in yanında ekstra bir kişi ile satışa sunmuş olduğu ve "
                                                             f"pazarda daha ucuzu bulunan ")


def empire_checker(item_name, current_price, item_wear):
    response = requests.get(f"https://csgoempire.gg/api/v2/trading/items?per_page=160&page=1&price_max_above=999999"
                            f"&search={item_name}&sort=asc&order=market_value").json()
    if len(response["data"]) == 1 and response["data"][0]["wear"] == item_wear:
        return True
    else:
        cheapest_item_in_market = response["data"][0]["market_value"]
        if len(str(cheapest_item_in_market)) == 4:
            cheapest_item_in_market = float(f"{str(cheapest_item_in_market)[:2]}." + f"{str(cheapest_item_in_market)[2:]}")
        elif len(str(cheapest_item_in_market)) == 5:
            cheapest_item_in_market = float(f"{str(cheapest_item_in_market)[:3]}." + f"{str(cheapest_item_in_market)[3:]}")
        else:
            cheapest_item_in_market = float(f"{str(cheapest_item_in_market)[:4]}." + f"{str(cheapest_item_in_market)[4:]}")

        if cheapest_item_in_market > current_price:
            return True
        elif current_price > cheapest_item_in_market and response["data"][0]["wear"] != item_wear:
            return False
        else:
            return True


def owner_checker(item_name, steam_dict):
    index = steam_dict["item_names"].index(item_name)
    owner = steam_dict["item_owner"][index]
    return owner


def message_sender(item_name, discount, item_current_price, item_url, extra_caption):
    requests.get(f"https://api.telegram.org/bot1997676317:AAF-EMTXHXcqTE20ZJQansGD2KbL9-8xxyI"
                 f"/sendPhoto?chat_id={CHAT_ID}&photo=https://community.cloudflare.steamstatic.com/economy/"
                 f"image/{item_url}&caption={extra_caption}{item_name}, Current Price: {item_current_price}, Disc: {discount}")

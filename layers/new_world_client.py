import backoff
import cloudscraper
import requests
from classes import AddProductsResponse


class NewWorldClient:
    __products_dict = {
        "butter": {
            "sale_type": "UNITS",
            "quantity": 1,
            "productid": "5002842-EA-000NW",
            "emoji": "🧈",
        },
        "eggs": {
            "sale_type": "UNITS",
            "quantity": 1,
            "productid": "5008394-EA-000",
            "emoji": "🥚",
        },
        "ice_cream_vanilla": {
            "productId": "5027951-EA-000",
            "quantity": 1,
            "sale_type": "UNITS",
            "emoji": "🍦",
        },
        "bacon": {
            "productId": "5266366-EA-000",
            "quantity": 1,
            "sale_type": "UNITS",
            "emoji": "🥓",
        },
        "standard_small_milk": {
            "productId": "5260707-EA-000NW",
            "quantity": 1,
            "sale_type": "UNITS",
            "emoji": "🥛",
        },
        "light_big_milk": {
            "productId": "5026265-EA-000NW",
            "quantity": 1,
            "sale_type": "UNITS",
            "emoji": "🍼",
        },
        "coffee": {
            "productId": "5024310_EA_000NW",
            "quantity": 1,
            "sale_type": "UNITS",
            "emoji": "☕️",
        },
        "potato": {
            "productId": "5045849-KGM-000",
            "quantity": 2,
            "sale_type": "UNITS",
            "emoji": "🥔",
        },
        "pumpkin": {
            "productId": "5275641-KGM-000NW",
            "quantity": 200,
            "sale_type": "WEIGHT",
            "emoji": "🎃",
        },
        "brocolli": {
            "productId": "5039956-EA-000",
            "quantity": 1,
            "sale_type": "UNITS",
            "emoji": "🥦",
        },
        "cauliflower_half": {
            "productId": "5275784-EA-000NW",
            "quantity": 1,
            "sale_type": "UNITS",
            "emoji": "🥬",
        },
        "carrots": {
            "productId": "5039965-KGM-000",
            "quantity": 5,
            "sale_type": "UNITS",
            "emoji": "🥕",
        },
        "apples": {
            "productId": "5046525-KGM-000",
            "quantity": 6,
            "sale_type": "UNITS",
            "emoji": "🍎",
        },
        "oranges": {
            "productId": "5045761-KGM-000",
            "quantity": 6,
            "sale_type": "UNITS",
            "emoji": "🍊",
        },
        "bananas": {
            "productId": "5290289_KGM_000NW",
            "quantity": 1,
            "sale_type": "UNITS",
            "emoji": "🍌",
        },
        "cranberry_juice": {
            "productId": "5012571-EA-000NW",
            "quantity": 1,
            "sale_type": "UNITS",
            "emoji": "🧃",
        },
        "pepsi_cans": {
            "productId": "5283385-EA-000NW",
            "quantity": 1,
            "sale_type": "UNITS",
            "emoji": "🥤",
        },
        "mince": {
            "productId": "5101189-KGM-000",
            "quantity": 800,
            "sale_type": "WEIGHT",
            "emoji": "🔪",
        },
        "chicken_drumsticks": {
            "productId": "5131223-KGM-000",
            "quantity": 800,
            "sale_type": "WEIGHT",
            "emoji": "🍗",
        },
        "ice_cream_creme_eggs": {
            "productId": "5280566-EA-000",
            "quantity": 1,
            "sale_type": "UNITS",
            "emoji": "🍨",
        },
        "burger_buns": {
            "productId": "5026009-EA-000",
            "quantity": 1,
            "sale_type": "UNITS",
            "emoji": "🍔",
        },
        "frozen_peas": {
            "productId": "5017855-EA-000NW",
            "quantity": 1,
            "sale_type": "UNITS",
            "emoji": "✌️",
        },
        "dog_food": {
            "productId": "5010333-EA-000NW",
            "quantity": 1,
            "sale_type": "UNITS",
            "emoji": "🐶",
        },
        "cat_snacks": {
            "productId": "5016211-EA-000NW",
            "quantity": 4,
            "sale_type": "UNITS",
            "emoji": "😽",
        },
        "toilet_paper": {
            "productId": "5030695-EA-000",
            "quantity": 1,
            "sale_type": "UNITS",
            "emoji": "🧻",
        },
        "kitchen_towels": {
            "productId": "5010350_EA_000NW",
            "quantity": 1,
            "sale_type": "UNITS",
            "emoji": "🗞",
        },
        "tissues": {
            "productId": "5216883-EA-000NW",
            "quantity": 1,
            "sale_type": "UNITS",
            "emoji": "🤧",
        },
        "family_chips": {
            "items": [
                {
                    "productId": "5272307_EA_000NW",  # Sticky Ribs
                    "quantity": 1,
                    "sale_type": "UNITS",
                },
                {
                    "productId": "5300123_EA_000NW",  # Salt & Vinegar
                    "quantity": 1,
                    "sale_type": "UNITS",
                },
                {
                    "productId": "5036437_EA_000NW",  # Doritos Cheese Supreme
                    "quantity": 1,
                    "sale_type": "UNITS",
                },
            ],
            "emoji": "🥔",
        },
        "family_chocolatebars": {
            "items": [
                {
                    "productId": "5005705-EA-000NW",  # Turkish
                    "quantity": 1,
                    "sale_type": "UNITS",
                },
                {
                    "productId": "5285014-EA-000NW",  # Caramilk
                    "quantity": 1,
                    "sale_type": "UNITS",
                },
                {
                    "productId": "5009824-EA-000NW",  # Fruit and Nut bar
                    "quantity": 1,
                    "sale_type": "UNITS",
                },
                {
                    "productId": "5005258-EA-000NW",  # Aero Bar
                    "quantity": 1,
                    "sale_type": "UNITS",
                },
                {
                    "productId": "5201585-EA-000",  # Whittaker's Berry & Biscuit
                    "quantity": 1,
                    "sale_type": "UNITS",
                },
            ],
            "emoji": "🍫",
        },
        "baby_wipes": {
            "productId": "5226419_EA_000NW",
            "quantity": 1,
            "sale_type": "UNITS",
            "emoji": "👼",
        },
        "nappy_bags": {
            "productId": "5019372_EA_000NW",
            "quantity": 1,
            "sale_type": "UNITS",
            "emoji": "🧷",
        },
        "onions": {
            "productId": "5045856-KGM-000NW",
            "quantity": 5,
            "sale_type": "UNITS",
            "emoji": "🧅",
        },
        "garlic": {
            "productId": "5266214-KGM-000",
            "quantity": 1,
            "sale_type": "UNITS",
            "emoji": "🧄",
        },
    }

    def __init__(self, username: str, password: str):
        self.token = self.__login(username, password)

    @classmethod
    def get_readable_products(self) -> list[str]:
        return [
            f'{product["emoji"]} {key.replace("_", " ").title()}'
            for key, product in self.__products_dict.items()
        ]

    @backoff.on_exception(backoff.expo, requests.exceptions.HTTPError, max_time=8)
    def add_products_to_basket(self, products: list[str]) -> AddProductsResponse:
        session = cloudscraper.create_scraper()

        products_to_add: list[str] = []

        for product_to_add in products:
            # This will take something like "🥔 Family Chips"
            # and make it into "family_chips"
            # FIX: would introduce a bug if input did not have an emoji.
            key_like_product = product_to_add.lower().replace(" ", "_")[2:]

            product = self.__products_dict.get(key_like_product)

            if product is None:
                continue
            elif product.get("items"):
                for nested_product_to_add in product["items"]:
                    products_to_add.append(nested_product_to_add)
            else:
                products_to_add.append(product)

        payload = {"products": products_to_add}

        cookies = {"SessionCookieIdV2": self.token}

        res = session.post(
            "https://www.newworld.co.nz/CommonApi/Cart/Index",
            json=payload,
            cookies=cookies,
        )

        res.raise_for_status()

        return AddProductsResponse.from_json(res.text)

    @backoff.on_exception(backoff.expo, requests.exceptions.HTTPError, max_time=8)
    def __login(self, username: str, password: str) -> str:
        payload = {"email": username, "password": password}

        session = cloudscraper.create_scraper()

        res = session.post(
            "https://www.newworld.co.nz/CommonApi/Account/Login", data=payload
        )

        res.raise_for_status()

        return res.cookies.get("SessionCookieIdV2")

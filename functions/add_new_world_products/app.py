import cloudscraper
import backoff
import requests

import schemas

from aws_lambda_powertools.utilities.validation import validator
from aws_lambda_powertools import Logger

logger = Logger(service="add_new_world_products")


class NewWorldClient():

    products_dict = {
        "butter": {
           "sale_type": "UNITS",
           "quantity": 1,
           "productid": "5002842-EA-000NW",
           "emoji": "🧈"
        },
        "eggs": {
           "sale_type": "UNITS",
           "quantity": 1,
           "productid": "5008394-EA-000",
           "emoji": ""
        },
        "ice_cream": {
           "sale_type": "UNITS",
           "quantity": 1,
           "productid": "5008394-EA-000",
           "emoji": ""
        }
        # Bacon
        # Milk
        # Coffee
        # Tea
        # Potato
        # Pumpkin
        # Brocolli
        # Colliflower
        # Carrots
        # Apples
        # Oranges
        # Bananas
        # Cranberry Juice
        # Pepsi Can
        # Mince
        # Chicken
        # Vanilla Ice Cream
        # Cream Egg Ice Cream
        # Burger Buns
        # Frozen Peas
        # Cocholate Bars
        # Dog Food
        # Cat Food
        # Toilet Paper
        # Kitchen Towels
        # Tissues
        # Family Chips
            # One Sticky Ribs
            # One Vinegar
            # One Doritus
        # Baby Wipes
        # Nappy Bags
        # Onion
        # Garlic
        # Dog Treat
    }

    def __init__(self, username, password):
        self.token = self.__login(username, password)

    def get_readable_products(self):
        return [x.replace("_", " ").title() for x in self.products_dict]

    @backoff.on_exception(backoff.expo,
                          requests.exceptions.HTTPError,
                          max_time=8)
    def add_products(self, products):
        session = cloudscraper.create_scraper()

        products_to_add = [self.products_dict[product.lower()] for product in products]

        payload = {
            'products': products_to_add
        }

        cookies = {
            'SessionCookieIdV2': self.token
        }

        res = session.post(
            "https://www.newworld.co.nz/CommonApi/Cart/Index",
            json=payload,
            cookies=cookies,
        )

        res.raise_for_status()

    @backoff.on_exception(backoff.expo,
                          requests.exceptions.HTTPError,
                          max_time=8)
    def __login(self, username, password):
        payload = {
              "email": username,
              "password": password
        }

        session = cloudscraper.create_scraper()

        res = session.post(
            "https://www.newworld.co.nz/CommonApi/Account/Login", data=payload)

        res.raise_for_status()

        return res.cookies.get("SessionCookieIdV2")


@validator(inbound_schema=schemas.INPUT)
@logger.inject_lambda_context
def lambda_handler(event, context):
    email = event['email']
    password = event['password']
    products = event['products']

    logger.info({
        "operation": "add products to the basket",
        "email": "********",
        "password": "********",
        "products": products
    })

    try:
        new_world_client = NewWorldClient(email, password)

        new_world_client.add_products(products)
    except requests.HTTPError as err:
        logger.exception(err)
        raise err

    logger.info(
        f'Successfully added {len(products)} products to New Worlds basket.')

    return {
        "products": products
    }

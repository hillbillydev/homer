import requests

import schemas

from new_world_client import NewWorldClient
from aws_lambda_powertools.utilities.validation import validator
from aws_lambda_powertools import Logger

logger = Logger(service="add_new_world_products")


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

        new_world_client.add_products_to_basket(products)
    except requests.HTTPError as err:
        logger.exception(err)
        raise err

    logger.info(
        f'Successfully added {len(products)} products to New Worlds basket.')

    return {
        "products": products
    }

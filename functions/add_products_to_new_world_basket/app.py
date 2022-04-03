from dataclasses import dataclass
from typing import Any, Dict

import requests
import schemas
from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.utilities.validation import validator
from dataclasses_json import dataclass_json
from new_world_client import NewWorldClient

logger = Logger(service="add_new_world_products")


@dataclass_json
@dataclass
class AddProductsToBasketRequest:
    email: str
    password: str
    products: list[str]  # ["🥚 Eggs", "🧈 Butter"]


@validator(inbound_schema=schemas.INPUT)
@logger.inject_lambda_context
def lambda_handler(event: Dict[str, Any], context: LambdaContext) -> Dict[str, Any]:
    parsed_event: AddProductsToBasketRequest = AddProductsToBasketRequest.from_dict(
        event
    )

    logger.info(
        {
            "operation": "add products to the basket",
            "email": "********",
            "password": "********",
            "products": parsed_event.products,
        }
    )

    try:
        new_world_client = NewWorldClient(parsed_event.email, parsed_event.password)

        res = new_world_client.add_products_to_basket(parsed_event.products)

    except requests.HTTPError as err:
        logger.exception(err)
        raise err

    logger.info(
        f"Successfully added {len(parsed_event.products)} products to New Worlds basket."
    )

    return {
        "products": parsed_event.products,
        "unavailable_products": len(res.unavailableProducts),
    }

import schemas
from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.validation import validator
from new_world_client import NewWorldClient

logger = Logger(service="get_readable_products")


@validator(outbound_schema=schemas.OUTPUT)
@logger.inject_lambda_context
def lambda_handler(event, context):
    readable_products = NewWorldClient.get_readable_products()

    logger.info(f"Successfully fetched {len(readable_products)} products.")

    return {"products": readable_products}
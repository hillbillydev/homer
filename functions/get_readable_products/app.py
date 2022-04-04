from typing import Any, Dict

import schemas
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.utilities.validation import validator
from new_world_client import NewWorldClient

logger = Logger()
tracer = Tracer()


@validator(outbound_schema=schemas.OUTPUT)
@logger.inject_lambda_context
@tracer.capture_lambda_handler
def lambda_handler(event: Dict[str, Any], context: LambdaContext) -> Dict[str, Any]:
    readable_products = NewWorldClient.get_readable_products()

    logger.info(f"Successfully fetched {len(readable_products)} products.")
    tracer.put_annotation("get_readable_products", "SUCCESS")

    return {"products": readable_products}

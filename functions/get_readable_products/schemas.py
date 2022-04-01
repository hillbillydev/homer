
OUTPUT = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "Sample outgoing readable products",
    "description": "The root schema comprises the entire JSON document.",
    "examples": [{"products": ["🥓 Bacon", "🥠 Family Chips"]}],
    "required": ["products"],
    "properties": {
        "products": {
            "$id": "#/properties/products",
            "type": "array",
            "uniqueItems": True,
            "examples": [["🥓 Bacon", "🥚 Eggs"]],
            "maxItems": 1000,
            "items": {
                "type": "string"
            }
        },
    },
}

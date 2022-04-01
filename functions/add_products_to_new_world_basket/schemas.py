
INPUT = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "Add New World Products",
    "description": "Data needed to add products into a basket.",
    "examples": [{
        "email": "john.doe@dev.com",
        "password": "janedoe123",
        "products": ["Eggs", "Bacon"]
    }],
    "required": ["email", "password", "products"],
    "properties": {
        "email": {
            "$id": "#/properties/email",
            "type": "string",
            "format": "email",
            "title": "The email",
            "examples": ["john.doe@dev.com"],
            "maxLength": 150,
        },
        "password": {
            "$id": "#/properties/password",
            "type": "string",
            "title": "The password",
            "examples": ["janedoe123"],
            "maxLength": 150,
        },
        "products": {
            "$id": "#/properties/products",
            "type": "array",
            "title": "A slice with all the products the user wants to add.",
            "examples": [["Bacon", "Eggs"]],
            "minItems": 1,
            "maxItems": 1000,
            "uniqueItems": True,
            "items": {
                "type": "string"
            },
        },
    },
}

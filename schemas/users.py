user = {
    "type": "object",
    'additionalProperties': False,
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "email": {"type": "string"},
                "first_name": {"type": "string"},
                "last_name": {"type": "string"},
                "avatar": {"type": "string"},
            },
            "required": ["id", "email", "first_name", "last_name", "avatar"],
        },
        "support": {
            "type": "object",
            "properties": {"url": {"type": "string"}, "text": {"type": "string"}},
            "required": ["url", "text"],
        },
    },
    "required": ["data", "support"],
}

create = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "id": {"type": "string"},
        "createdAt": {"type": "string"},
    },
    "required": ["id", "createdAt"],
}


update = {
    "type": "object",
    'additionalProperties': False,
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "updatedAt": {"type": "string"},
    },
    "required": ["job", "updatedAt"],
}
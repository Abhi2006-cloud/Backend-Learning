import secrets

api_keys = {}

def generate_api_key(app_name: str):
    key = secrets.token_hex(32)
    api_keys[key] = app_name
    return key

def validate_api_key(key: str):
    return api_keys.get(key)


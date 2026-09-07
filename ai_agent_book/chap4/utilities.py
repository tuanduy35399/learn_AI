import json

def to_json(s):
    try:
        return json.load()
    except Exception:
        return {}
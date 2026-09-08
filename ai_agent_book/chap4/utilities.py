import json

def to_obj(s):
    try:
        return json.loads(s) #từ json sang dict
    #nếu muốn từ dict về json thì dùng json.dumps(s)
    except Exception:
        return {}
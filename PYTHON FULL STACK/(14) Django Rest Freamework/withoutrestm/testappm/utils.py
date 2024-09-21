import json

def is_json(data):
    try:
        p_Data = json.loads(data)
        valid = True
    except ValueError:
        valid = False
    return valid 

def obj_to_dict(obj):
    obj_dict = {}
    for key, value in obj.__dict__.items():
        if not key.startswith('_'):
            obj_dict[key] = value
    return obj_dict
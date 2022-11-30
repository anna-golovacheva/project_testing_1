def get_val(collection, key, default):
    try:
        return collection[key]
    except KeyError:
        return default

def set_(coll, path, value):
    if path:
        k = path.pop(0)
        if coll.get(k):
            if path:
                return set_(coll[k], path, value)
            else:
                coll[k] = value

        else:
            if path:
                coll[k] = {}
                return set_(coll[k], path, value)
            else:
                coll[k] = value

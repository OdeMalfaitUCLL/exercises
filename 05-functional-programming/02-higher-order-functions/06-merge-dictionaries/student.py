def merge_dictionaries(d1,d2,merge_function):
    result = dict(d1)
    for k,v in d2.items():
        if k in result:
            v1 = d1.get(k)
            v2 = d2.get(k)
            result[k] = merge_function(v1,v2)
        else: result[k] = v
    return result
        
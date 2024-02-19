# Write your code here
def keys_with_value(d,value):
    new = []
    for k,v in d.items():
        if v == value:
            new.append(k)
    return new
print(keys_with_value({'a': 1, 'b': 2, 'c': 1}, 1))


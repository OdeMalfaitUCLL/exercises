# Write your code here
def double_dict_values(d):
    new = {}
    for k,v in d.items():
        new[k] = v * 2
    return new

print(double_dict_values({'a': 1, 'b': 2, 'c': 3}))
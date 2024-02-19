# Write your code here
def odd_keys_dict(d):
    new = {}
    for x,y in d.items():
        if x % 2 != 0:
         new[x] = y
    return new
print(odd_keys_dict({1: 'a', 2: 'b', 3: 'c'}))
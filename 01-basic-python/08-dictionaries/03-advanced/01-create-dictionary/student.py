# Write your code here
def create_dictionary(list1,list2):
    d = {}
    for i in range(len(list1)):
        d[list1[i]] = list2[i]
    return d

print(create_dictionary(['a', 'b', 'c'], [1, 2, 3]))
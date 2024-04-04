def indices_of(xs,condition):
    counter = 0
    result = []
    while counter < len(xs):
        if condition(xs[counter]):
            result.append(counter)
        counter +=1
    return result

# def is_odd(x):
#     return x % 2 != 0

# print(indices_of([1, 2, 3, 4, 5, 6, 7, 8], is_odd))
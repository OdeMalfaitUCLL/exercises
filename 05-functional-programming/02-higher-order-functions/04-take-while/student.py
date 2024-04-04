def take_while(xs, condition):
    counter = 0
    while counter < len(xs) and condition(xs[counter]):
            counter += 1
    return (xs[:counter],xs[counter:])

# def is_negative(x):
#     return x < 0

# print(take_while([-4, -2, 0, -1, 4, 6],is_negative))

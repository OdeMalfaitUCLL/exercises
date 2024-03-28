def cycle(xs):
    lst = list(xs)
    while True:
        for value in lst:
            yield value

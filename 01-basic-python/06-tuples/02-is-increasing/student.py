# Write your code here
def is_increasing(ns):
    ms = ns[1:]
    new = list(zip(ns,ms))
    for (x,y) in new:
        if x > y:
            return False
    return True

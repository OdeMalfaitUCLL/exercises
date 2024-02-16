# Write your code here
def target_sum(ns, target):
    sum = 0
    for x in ns:
        for y in ns:
            if x + y == target:
                return True
    return False
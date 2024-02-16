# Write your code here
def contains_duplicates(xs):
    teller = 0
    for i in xs: 
        count = xs.count(i)
        if count > 1:
            teller +=1
    if teller >= 1:
        return True
    else: return False
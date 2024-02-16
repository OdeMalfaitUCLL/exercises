# Write your code here
def digit_sum(n):
    sum=0
    for i in str(n):
        sum+=int(i)
    return sum

def last_digit(n):
    return n%10

def remove_last_digit(n):
    return n//10

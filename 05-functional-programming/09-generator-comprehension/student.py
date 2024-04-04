from itertools import count
def is_prime(n):
    #de all() checkt of n niet gedeeld kan worden door cijfers tussen 2 en n-1
    #priemgetal moet groter zijn dan 1, daarom n >= 2
    return n >= 2 and all(n%x != 0 for x in range(2,n))

def primes():
    #count(2); deze oneindige generator begint bij getal 2 (priemgetallen zijn > 2)
    return (n for n in count(2) if is_prime(n))




print(is_prime(5))
print(is_prime(6))
# ps = primes()
# print(next(ps))
# print(next(ps))
# print(next(ps))
# print(next(ps))
# print(next(ps))
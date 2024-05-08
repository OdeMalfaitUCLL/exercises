def sum_numbers(number):
    n = str(abs(number))
    if int(n) < 10:
        return number
    else:
        new_number = int(n[1:])
        return int(n[0]) + sum_numbers(new_number)

print(sum_numbers(234))
print(sum_numbers(-153))
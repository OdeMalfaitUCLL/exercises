
# Write your code here
import re
def contains_three_digits(string):
    return re.fullmatch(r".*[0-9].*[0-9].*[0-9].*",string)
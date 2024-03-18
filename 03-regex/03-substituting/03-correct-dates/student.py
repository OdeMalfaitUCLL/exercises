# Write your code here
import re
def correct_dates(string):
    return re.sub(r"([0-9]+)/([0-9]+)/([0-9]+)", r"\2/\1/\3",string)
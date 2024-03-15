# Write your code here
import re
def is_valid_password(string):
    positive_regex = [
        r".{12}",
        r"[0-9]",
        r"[a-z]",
        r"[A-Z]",
        r"[+-*/.@]",
    ]
    negative_regex = [
        r"(.)\1{2}",
        r"(.)(.*\1){3}"
    ]
    for regex in positive_regex:
        if not re.search(regex,string):
            return False
    for regex in negative_regex:
        if re.search(regex,string):
            return False
    return True
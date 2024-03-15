# Write your code here
import re
def scrape_email_addresses(string):
    return re.findall(r"[0-9a-zA-Z.]+@[0-9a-zA-Z.]+",string)
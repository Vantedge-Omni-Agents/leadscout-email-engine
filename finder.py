import requests
import re

url = input("Enter website URL: ")

html = requests.get(url, timeout=10).text

emails = set(
    re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        html
    )
)

for email in emails:
    print(email)

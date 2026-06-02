import requests
import re

website = input("Enter website URL: ").strip()

if not website.startswith("http"):
website = "https://" + website

try:
response = requests.get(website, timeout=10)

```
emails = set(
    re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        response.text
    )
)

print("\nEmails Found:")

if emails:
    for email in emails:
        print("-",
```

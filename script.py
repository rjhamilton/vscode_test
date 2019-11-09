import requests

r = requests.get("https://python.org")
print(r.status_code)
print(r.ok)

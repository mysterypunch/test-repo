import requests


r = requests.get('https://www.espn.com')
print(r.status_code)

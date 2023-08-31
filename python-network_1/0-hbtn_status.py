"""A module that fetches the status of a website using the requests library"""

import requests

url="https/alu-intranet.htbn.io/status"
response = requests.get(url)

if response.status_code == 200:
    print("Body response")
    print("\t-type:",type(response.text))
    print("\t-content:", response.text)
else:
    print("Error fetcheing website. Status code:, response.status_code")

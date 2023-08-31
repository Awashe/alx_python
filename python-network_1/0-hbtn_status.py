"""
A module that fetches the status of a website using the requests library.
This code module uses the `requests` library to send an HTTP GET request to a specified URL and checks the status code of the returned response. If the status code is 200, indicating that the request was successful, the code prints the body of the response to the console in a formatted manner. If the status code is not 200, indicating a failure, an error message is printed to the console along with the actual status code returned by the server.
"""
import requests

url="https/alu-intranet.htbn.io/status"
response = requests.get(url)

if response.status_code == 200:
    print("Body response")
    print("\t-type:",type(response.text))
    print("\t-content:", response.text)
else:
    print("Error fetcheing website. Status code:, response.status_code")

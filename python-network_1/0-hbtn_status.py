"""
A module that fetches the status of a website using the requests library.

This module defines a function that sends a GET request to a specified URL and displays
the body of the response, including its type and content. It uses the requests library,
so this library must be installed to use the function.

Example:
    To fetch the status of the website https://alu-intranet.hbtn.io/status, use the
    following code:

        import status_checker

        url = "https://alu-intranet.hbtn.io/status"
        status_checker.check_status(url)

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

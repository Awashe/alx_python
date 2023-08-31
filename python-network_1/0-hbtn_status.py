"""The code module uses the `requests` library to send an HTTP GET request to a specified URL and checks the status code of the returned response. If the status code is 200, indicating that the request was successful, the code prints the body of the response to the console in a formatted manner. If the status code is not 200, indicating a failure, an error message is printed to the console along with the actual status code returned by the server.

The purpose of this code module is to perform a basic status check of a web application by sending an HTTP GET request and checking its response status code. This code can be used standalone or integrated as part of a larger application to perform regular or automated web application checks.

To use this module, the user needs to import the `requests` library and provide a URL to check. The code retrieves and prints the content of the response if the status code is 200, providing useful information for debugging or testing purposes. If the status code is not 200, an error message is printed to the console to indicate the failure."""
import urllib.request

url = 'https://alu-intranet.htbn.io/status'

try:
    with urllib.request.urlopen(url) as response:
        if response.getcode() == 200:
            print("Body response")
            print("\t-type:", type(response.read().decode('utf-8')))
            print("\t-content:", response.read().decode('utf-8'))
        else:
            print("Error fetching website. Status code:", response.getcode())
except:
    print("Could not connect to the URL")

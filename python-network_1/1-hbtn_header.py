import requests
import sys

"""
Module to get X-Request-Id from the response header of a URL.
"""

def get_X_Request_Id(url: str) -> str:
    """
    Function to get the value of X-Request-Id from the response header of a URL.

    Parameters:
    url (str): The URL to send the request to.

    Returns:
    str: The value of X-Request-Id in the response header.
    """
    try:
        response = requests.get(url)
        x_request_id = response.headers['X-Request-Id']
        return x_request_id
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    url = input("Enter the URL: ")
    x_request_id = get_X_Request_Id(url)
    print(f"The value of X-Request-Id in the response header is: {x_request_id}")
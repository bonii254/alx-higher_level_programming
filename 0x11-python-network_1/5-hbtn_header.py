#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header"""

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    req = requests.get(url)
    X_Request_Id = req.headers.get("X-Request-Id")
    print("{}".format(X_Request_Id))

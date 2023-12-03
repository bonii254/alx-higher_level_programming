#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the
URL and displays the value of the X-Request-Id variable found
in the header of the response."""

if __name__ == "__main__":
    import urllib.request
    import sys

    if len(sys.argv) < 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        exit(1)
    url = sys.argv[1]
    with urllib.request.urlopen(url) as res:
        X_Request_Id = res.headers.get("X-Request-Id")
        print("{}".format(X_Request_Id))

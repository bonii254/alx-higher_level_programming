#!/usr/bin/python3
""" a Python script that takes in a URL, sends a request to
the URL and displays the body of the response (decoded in utf-8).
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    if len(sys.argv) < 2:
        print("Usage: {} <url>".format(sys.argv[0]))
        exit(1)

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            body = res.read().decode("utf-8")
            print("{}".format(body))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))

#!/usr/bin/python3
""" Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)"""

if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    if len(sys.argv) < 3:
        print("Usage: {} <url> <email>".format(sys.argv[0]))
        exit(1)
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}
    data = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        body = res.read().decode("utf-8")
        print("{}".format(body))

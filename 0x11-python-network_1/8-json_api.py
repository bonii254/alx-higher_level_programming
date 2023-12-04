#!/usr/bin/python3
"""a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) < 2:
        letter = ""
    else:
        letter = sys.argv[1]
    param = {"q": letter}
    req = requests.post("http://0.0.0.0:5000/search_user", data=param)
    try:
        res = req.json()
        if res:
            print("[{}] {}".format(res.get("id"), res.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

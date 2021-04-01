import requests
import time


def dock():
    time.sleep(2)
    url = 'http://192.168.1.248/amr/public/controls/docking/magnetic'
    payload = '''{
        "max_vtheta": 0.0,
        "direction": "forward",
        "name": "forward",
        "max_vx": 0.1,
        "slow_vx": 0.0,
        "slow_vtheta": 0.0,
        "is_safety_active": false,
        "is_docking": true
    }'''
    headers = {
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
        "Postman-Token": "b284e43b-c500-45b6-8962-c29a88c9f2af"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    if response.status_code >= 400:
        return False
    get_url = "http://192.168.1.248/amr/public/status/docking"
    while True:
        try:
            response = requests.get(get_url)
            if response.status_code >= 400:
                return False
            data = response.json()
            if not data["status"] == "docking":
                if data["status"] == "successful":
                    print("done")
                    return True
                else:
                    print("fail")
                    return False
            time.sleep(1)
        except Exception as e:
            print("docking failed", e)
    return false


print(dock())

import requests
import time


def dock():
    time.sleep(2)
    url = 'http://192.168.1.248/amr/public/controls/docking/fixed'
    payload = '''{
        "max_vtheta": 0.0,
        "direction": "forward",
        "name": "moveamr",
        "max_vx": 0.1,
        "frame" : "moveamr",
        "goal_angular_tolerance" : 0.0,
        "goal_distance_tolerance" : 0.0,
        "is_docking": true,
        "is_safety_active": true,
        "theta": 0.0,
        "y": -0.16,
        "x": -0.17,
        "is_goal_stored" : true
    }'''
    headers = {
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
        "Postman-Token": "b284e43b-c500-45b6-8962-c29a88c9f2af"
    }
    response = requests.post(url, payload, headers)
    print(response.text)

    if response.status_code >= 400:
        return False
    get_url = 'http://192.168.1.248/amr/public/status/docking'
    while True:
        try:
            response = requests.get(get_url)
            if response.status_code >= 400:
                return False
            data = response.json()
            if not data["status"] == "docking":
                if data["status"] == "successful":
                    print("docked successfully")
                    return True
                else:
                    print("unsuccessful")
                    return False
            time.sleep(1)
        except Exception as e:
            print("docking failed", e)
    return false


print(dock())

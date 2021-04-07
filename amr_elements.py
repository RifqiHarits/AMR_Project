# Progress 6
# Last Updated: 7 April 2021
# Made by Rifqi
# AMR Version: 1.2.2
# Refer to "Public Client Interface for the SESTO Element Server" Manual for AMRServerElement Class
# Refer to "Public Interface for SESTO Element AMRs" Manual for AMRElement Class

# For any error, please check the output, there will be a code_status and refer to HTTP Code Responses
# to troubleshoot for errors occurred using class. Please check your url appends if it is written correctly
# based on the manuals and check your data sent for put and post operations.
# If service is unavailable, it might be due it not being updated to the latest firmware.
# If it is not updated please get help for instructions on updating the firmware.

# Below are some examples of how to use the Classes
# AMRServerElement().get_json('/goals')
# AMRServerElement().post_json('/example', {'example': 'example'})
# AMRServerElement().put_json('/example', {'example': 'example'})
# AMRElement().get_json('/status/batteries')
# AMRElement().post_json('/example', {'example': 'example'})
# AMRElement().put_json('/example', {'example': 'example'})

import requests
import json
import time


class AMRServerElement:
    @staticmethod
    def wait(sec=0):
        time.sleep(sec)

    def pingable(self):
        try:
            requests.get('http://' + self.ip)
        except Exception as e:
            print(e)
            self.pingable_result = False
            return False
        else:
            self.pingable_result = True
            return True

    def request_token(self):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + "/public/auth"
        headers = {
            "user_name": "{}".format(self.username),  # insert username
            "password": "{}".format(self.password)  # insert password
        }
        r = requests.post(url, None, headers)
        if r.status_code >= 400:
            self.token = "invalid"
            self.authorization = "invalid"
            return
        self.token = r.json()['access_token']
        self.authorization = {
            'Authorization': 'Bearer {}'.format(self.token),
            'Content-Type': 'application/json',
            "Cache-Control": "no-cache"
        }

    def __init__(self, ip="192.168.0.249", username="admin", password="P@ssword123"):
        self.username = username
        self.password = password
        self.ip = ip
        headers = {
            "user_name": "{}".format(username),  # insert username
            "password": "{}".format(password)  # insert password
        }
        url = 'http://' + ip + "/public/auth"
        if not self.pingable():
            self.pingable_result = False
            return
        r = requests.post(url, None, headers)
        if r.status_code >= 400:
            self.token = "invalid"
            self.authorization = "invalid"
            return
        self.token = r.json()['access_token']
        self.authorization = {
            'Authorization': 'Bearer {}'.format(self.token),
            'Content-Type': 'application/json',
            "Cache-Control": "no-cache"
        }

    def get_json(self, url_append):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/public'
        url = url + url_append
        r = requests.get(url, headers=self.authorization)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()

    def post_json(self, url_append, data):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/public'
        url = url + url_append
        r = requests.post(url, json.dumps(data), headers=self.authorization)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()

    def put_json(self, url_append, data):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/public'
        url = url + url_append
        r = requests.put(url, json.dumps(data), headers=self.authorization)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()

    def get_pauses(self):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/public'
        url = url + '/amrs/pause'
        r = requests.get(url, headers=self.authorization)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()

    def pause_amrs(self, amr_ids=[]):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/public'
        url = url + '/amrs/pause'
        data = {
            "ids": amr_ids,
            "status": "paused"
        }
        r = requests.put(url, json.dumps(data), headers=self.authorization)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()

    def resume_amrs(self, amr_ids=[]):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/public'
        url = url + '/amrs/pause'
        data = {
            "ids": amr_ids,
            "status": "operational"
        }
        r = requests.put(url, json.dumps(data), headers=self.authorization)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()

    def get_modes(self):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/public'
        url = url + '/amrs/mode'
        r = requests.get(url, headers=self.authorization)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()

    def get_idle_release_statuses(self):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/public'
        url = url + '/amrs/release/idle'
        r = requests.get(url, headers=self.authorization)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()

    def get_station_release_statuses(self):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/public'
        url = url + '/amrs/release/station'
        r = requests.get(url, headers=self.authorization)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()

    def get_statuses(self):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/public'
        url = url + '/amrs/statuses'
        r = requests.get(url, headers=self.authorization)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()

    def get_users(self):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/public'
        url = url + '/users'
        r = requests.get(url, headers=self.authorization)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()

    def get_version(self):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/public'
        url = url + '/deployment/binaries'
        r = requests.get(url, headers=self.authorization)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()[0]['version']

    def get_graphs(self):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/public'
        url = url + '/graphs'
        r = requests.get(url, headers=self.authorization)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()

    def get_maps(self):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/public'
        url = url + '/maps'
        r = requests.get(url, headers=self.authorization)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()

    '''
    def send_recovery(self, amr_id, waypoint_id, amr_footprint):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/public'
        url = url + '/amrs/recovery'
        data = {
            "id": amr_id,  # AMR ID
            "waypoint": waypoint_id,  # WAYPOINT ID
            "battery": {"high": 80.0, "low": 40.0},
            "categorical_speed": {"low": 0.3, "medium": 0.7, "high": 1.2},
            "charging_mode": ["acsv", "hcse"],
            "directionality": "bi",
            "footprint": amr_footprint,
            "max_speed": speed,
            "created_by": "fleet"  # CREATED BY FLEET AND NOT MISSION
        }
        r = requests.post(url, json.dumps(data), headers=self.authorization)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()
    '''

    def send_goal(self, amr_id, graph_id, waypoint_id):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/public'
        url = url + '/goals'
        data = {
            "amr_id": amr_id,  # AMR ID
            "graph_id": graph_id,  # MAP GRAPH ID
            "waypoint_id": waypoint_id,  # WAYPOINT ID
            "created_by": "fleet"  # CREATED BY FLEET AND NOT MISSION
        }
        r = requests.post(url, json.dumps(data), headers=self.authorization)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()

    def station_release(self, amr_id):
        if not self.pingable_result:
            return
        statuses = self.get_station_release_statuses()
        if statuses is None or statuses is False:
            time.sleep(0.5)
            self.station_release(amr_id)
            return
        try:
            try_val = statuses[0]["id"]
            try_val2 = statuses[1]["id"]
        except Exception as e:
            print(e)
            time.sleep(0.5)
            self.station_release(amr_id)
            return
        else:
            del try_val
            del try_val2

        for i in range(len(statuses)):
            if statuses[i]["id"] == amr_id:
                if statuses[i]["status"] == "released":
                    return
        url = 'http://' + self.ip + '/public'
        url = url + '/amrs/release/station'
        data = {
            "id": amr_id,  # AMR ID
            "status": "released",  # RELEASE STATUS
            "created_by": "fleet"  # CREATED BY FLEET AND NOT MISSION
        }
        r = requests.post(url, json.dumps(data), headers=self.authorization)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()

    def idle_release(self, amr_id):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/public'
        url = url + '/amrs/release/idle'
        data = {
            "id": amr_id,  # AMR ID
            "status": "released",  # RELEASE STATUS
            "created_by": "fleet"  # CREATED BY FLEET AND NOT MISSION
        }
        r = requests.put(url, json.dumps(data), headers=self.authorization)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()

    def get_waypoint(self, amr_id):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/public'
        url = url + '/amrs/statuses'
        r = requests.get(url, headers=self.authorization)
        # print('Status Code: {}'.format(r.status_code))
        try:
            r.json()
        except Exception as e:
            print(e)
            return False
        else:
            data = r.json()
            for i in range(len(data)):
                if data[i]["amr_id"] == amr_id:
                    return data[i]["curr_waypoint_id"]
            return False

    def wait_reached_waypoint(self, amr_id, waypoint_id):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/public'
        url = url + '/amrs/statuses'
        r = requests.get(url, headers=self.authorization)
        # print('Status Code: {}'.format(r.status_code))
        try:
            r.json()
        except Exception as e:
            print(e)
            return False
        else:
            data = r.json()
            amr_exist = False
            amr_reached = False
            for i in range(len(data)):
                if data[i]["amr_id"] == amr_id:
                    amr_exist = True
                    if data[i]["curr_waypoint_id"] == waypoint_id:
                        if data[i]["navigation_state"] == "navigating":
                            break
                        else:
                            return True
                    else:
                        break
            if amr_exist:
                if not amr_reached:
                    time.sleep(0.5)
                self.wait_reached_waypoint(amr_id, waypoint_id)
            else:
                return False

    def send_goal_auto_release(self, amr_id, graph_id, waypoint_id):
        self.send_goal(amr_id, graph_id, waypoint_id)
        self.wait_reached_waypoint(amr_id, waypoint_id)
        self.station_release(amr_id)

    def send_idle_wait_reached(self, amr_id):
        self.idle_release(amr_id)
        waypoint_id = 0
        goals = self.get_json('/goals')
        for i in range(len(goals)):
            if goals[i]['amr_id'] == amr_id:
                waypoint_id = goals[i]['waypoint_id']
                break
        if waypoint_id == 0:
            return False
        self.wait_reached_waypoint(amr_id, waypoint_id)
        return True


class AMRElement:
    @staticmethod
    def wait(sec=0):
        time.sleep(sec)

    def pingable(self):
        try:
            requests.get('http://' + self.ip)
        except Exception as e:
            print(e)
            self.pingable_result = False
            return False
        else:
            self.pingable_result = True
            return True

    def __init__(self, ip="192.168.1.248"):
        self.ip = ip
        if not self.pingable():
            self.pingable_result = False
            return
        self.headers = {
            "Content-Type": "application/json",
            "Cache-Control": "no-cache",
            "Postman-Token": "b284e43b-c500-45b6-8962-c29a88c9f2af"
        }

    def get_json(self, url_append):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/amr/public'
        url = url + url_append
        r = requests.get(url)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()

    def post_json(self, url_append, data):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/amr/public'
        url = url + url_append
        r = requests.post(url, json.dumps(data), headers=self.headers)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()

    def put_json(self, url_append, data):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/amr/public'
        url = url + url_append
        r = requests.put(url, json.dumps(data), headers=self.headers)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()

    def get_released(self):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/amr/public'
        url = url + '/controls/release/station'
        r = requests.get(url)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            if r.json()['status'] == 'released':
                return True
            else:
                return False

    def wait_released(self):
        if not self.pingable_result:
            return
        while not self.get_released():
            time.sleep(0.1)
        return True

    def get_paused(self):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/amr/public'
        url = url + '/controls/pause'
        r = requests.get(url)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            if r.json()['status'] == 'paused':
                return True
            else:
                return False

    def pause_amr(self):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/amr/public'
        url = url + '/controls/pause'
        data = {
            "status": "paused"
        }
        r = requests.post(url, json.dumps(data), headers=self.headers)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()

    def resume_amr(self):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/amr/public'
        url = url + '/controls/pause'
        data = {
            "status": "operational"
        }
        r = requests.post(url, json.dumps(data), headers=self.headers)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()

    def get_battery_status(self):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/amr/public'
        url = url + '/status/batteries'
        r = requests.get(url)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()

    def get_main_battery_percentage(self):
        status = self.get_battery_status()
        if status:
            return status["battery_statuses"][0]["percentage"]
        else:
            return False

    def get_amr_id(self):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/amr/public'
        url = url + '/status/info/amr_id'
        r = requests.get(url)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()['id']

    def get_amr_name(self):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/amr/public'
        url = url + '/status/info/amr_name'
        r = requests.get(url)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()['name']

    def get_input_pin(self, pin=1):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/amr/public'
        url = url + '/controls/slot0/di/pin{}'.format(pin)
        r = requests.get(url)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()['pin{}'.format(pin)]

    def get_input_pin_all(self):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/amr/public'
        url = url + '/controls/slot0/di'
        r = requests.get(url)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()

    def get_output_pin(self, pin=1):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/amr/public'
        url = url + '/controls/slot0/do/pin{}'.format(pin)
        r = requests.get(url)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()['pin{}'.format(pin)]

    def get_output_pin_all(self):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/amr/public'
        url = url + '/controls/slot0/do'
        r = requests.get(url)
        print('Status Code: {}'.format(r.status_code))
        try:
            print("JSON from {}:".format(url))
            print(r.json())
        except Exception as e:
            print(e)
            return False
        else:
            return r.json()

    def mag_dock_backward(self):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/amr/public'
        url = url + "/controls/docking/magnetic"

        data = '{"max_vtheta" : 0.0, "direction" : "backward", "name" : "backward", "max_vx" : 0.1, "slow_vx" : 0.0, "slow_vtheta" : 0.0, "is_safety_active" : false, "is_docking" : true}'

        r = requests.post(url, json.dumps(data), headers=self.headers)

        print(r.text)

        if r.status_code >= 400:
            return False

        get_url = 'http://' + self.ip + '/amr/public' + "/status/docking"

        while True:
            try:
                r = requests.get(get_url)
                if r.status_code >= 400:
                    return False
                data = r.json()
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
                return False

    def mag_dock_forward(self):
        if not self.pingable_result:
            return
        url = 'http://' + self.ip + '/amr/public'
        url = url + "/controls/docking/magnetic"

        data = '{"max_vtheta" : 0.0, "direction" : "forward", "name" : "forward", "max_vx" : 0.1, "slow_vx" : 0.0, "slow_vtheta" : 0.0, "is_safety_active" : false, "is_docking" : true}'

        r = requests.post(url, json.dumps(data), headers=self.headers)

        print(r.text)

        if r.status_code >= 400:
            return False

        get_url = 'http://' + self.ip + '/amr/public' + "/status/docking"

        while True:
            try:
                r = requests.get(get_url)
                if r.status_code >= 400:
                    return False
                data = r.json()
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
                return False

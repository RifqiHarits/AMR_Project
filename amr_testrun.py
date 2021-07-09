import requests


def auth_amr(username="admin", password="P@ssword123", ip="192.168.0.249"):
    headers = {
        "user_name": "{}".format(username),  # insert username
        "password": "{}".format(password)  # insert password
    }
    url = 'http://' + ip + "/public/auth"
    r = requests.post(url, None, headers)
    if r.status_code >= 400:
        self.token = "invalid"
        self.authorization = "invalid"
        return None
    self.token = r.json()['access_token']
    self.authorization = {'Authorization': 'Bearer {}'.format(self.token)}


auth_amr()
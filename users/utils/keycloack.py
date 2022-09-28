import requests
import json
from urllib.parse import urljoin

from utils.environments import Environment, EnvKeys


class KeycloackClient:

    def __init__(self):
        environ = Environment()
        self.realm = "unicheck"
        self.keycloak_url = environ.get(EnvKeys.KEYCLOAK_URL)
        self.client_id = environ.get(EnvKeys.KEYCLOAK_CLIENT_ID)
        self.client_secret = environ.get(EnvKeys.KEYCLOAK_CLIENT_SECRET)
        self.token = None

    def connect(self):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json"
        }

        data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }

        url = self.keycloak_url + "/realms/" + self.realm + "/protocol/openid-connect/token"

        session = requests.session()
        r = session.post(url=url, headers=headers, data=data)

        if r.status_code == 200:
            result = r.json()
            self.token = result["token_type"] + " " + result["access_token"]

    def verify_token(self, token):
        headers = {
            "Authorization": token,
            "Accept": "application/json"
        }

        url = urljoin(self.keycloak_url, "/realms/{}/protocol/openid-connect/userinfo".format(self.realm))

        session = requests.session()
        r = session.post(url=url, headers=headers)
        result = None

        try:
            result = r.json()
        except:
            pass

        return r.status_code, result

    def get(self, keycloak_path: str):
        headers = {
            "Authorization": self.token,
            "Accept": "application/json"
        }

        keycloak_path = keycloak_path.replace('$REALM', self.realm)
        url = urljoin(self.keycloak_url, keycloak_path)

        session = requests.session()
        r = session.get(url=url, headers=headers)
        result = None

        try:
            result = r.json()
        except:
            pass

        return r.status_code, result

    def post_json(self, keycloak_path: str, data):
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.token,
            "Accept": "application/json"
        }

        keycloak_path = keycloak_path.replace('$REALM', self.realm)
        url = urljoin(self.keycloak_url, keycloak_path)

        session = requests.session()
        r = session.post(url=url, headers=headers, json=data)
        result = None

        try:
            result = r.json()
        except:
            pass

        return r.status_code, result

    def post_encoded(self, keycloak_path: str, data):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": self.token,
            "Accept": "application/json"
        }

        keycloak_path = keycloak_path.replace('$REALM', self.realm)
        url = urljoin(self.keycloak_url, keycloak_path)

        session = requests.session()
        r = session.post(url=url, headers=headers, data=data)
        result = None

        try:
            result = r.json()
        except:
            pass

        return r.status_code, result

    def put(self, keycloak_path: str, data):
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.token,
            "Accept": "application/json"
        }

        keycloak_path = keycloak_path.replace('$REALM', self.realm)
        print(keycloak_path)
        url = urljoin(self.keycloak_url, keycloak_path)

        session = requests.session()
        r = session.put(url=url, headers=headers, json=data)
        result = None

        try:
            result = r.json()
        except:
            pass

        return r.status_code, result

    def delete(self, keycloak_path: str):
        headers = {
            "Authorization": self.token,
            "Accept": "application/json"
        }

        keycloak_path = keycloak_path.replace('$REALM', self.realm)
        url = urljoin(self.keycloak_url, keycloak_path)

        session = requests.session()
        r = session.delete(url=url, headers=headers)
        result = None

        try:
            result = r.json()
        except:
            pass

        return r.status_code, result

    def disconnect(self):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": self.token,
            "Accept": "application/json"
        }

        url = self.keycloak_url + "/realms/" + self.realm + "/protocol/openid-connect/logout"

        session = requests.session()
        r = session.post(url=url, headers=headers)

        if r.status_code == 200:
            print("DISCONNECTED")


import os

from utils.exceptions import EnvironmentNotProvided, InvalidEnvironment
from enum import Enum

__creator__ = "IsaacBernardes"
__last_modifier__ = "IsaacBernardes"
__last_modify__ = "22/09/2022"
__version__ = open("version").read()


class EnvKeys(Enum):
    DB_HOST = "DB_HOST",
    DB_PORT = "DB_PORT",
    DB_USER = "DB_USER",
    DB_PASS = "DB_PASS",
    DB_NAME = "DB_NAME",
    KEYCLOAK_URL = "KEYCLOAK_URL",
    KEYCLOAK_CLIENT_ID = "KEYCLOAK_CLIENT_ID",
    KEYCLOAK_CLIENT_SECRET = "KEYCLOAK_CLIENT_SECRET",
    SERVER_HOST = "SERVER_HOST",
    SERVER_PORT = "SERVER_PORT",
    PROD = "PROD"


class Environment:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Environment, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self._environments = {}
        self.build_environments()

    def build_environments(self):
        expected_environments = [
            {"key": EnvKeys.DB_HOST, "type": str, "required": False, "default_value": None},
            {"key": EnvKeys.DB_PORT, "type": int, "required": False, "default_value": 5432},
            {"key": EnvKeys.DB_USER, "type": str, "required": False, "default_value": None},
            {"key": EnvKeys.DB_PASS, "type": str, "required": False, "default_value": None},
            {"key": EnvKeys.DB_NAME, "type": str, "required": False, "default_value": None},
            {"key": EnvKeys.KEYCLOAK_URL, "type": str, "required": True, "default_value": None},
            {"key": EnvKeys.KEYCLOAK_CLIENT_ID, "type": str, "required": True, "default_value": None},
            {"key": EnvKeys.KEYCLOAK_CLIENT_SECRET, "type": str, "required": True, "default_value": None},
            {"key": EnvKeys.SERVER_HOST, "type": str, "required": False, "default_value": "0.0.0.0"},
            {"key": EnvKeys.SERVER_PORT, "type": int, "required": False, "default_value": 8090},
            {"key": EnvKeys.PROD, "type": str, "required": False, "default_value": False}
        ]

        for env in expected_environments:

            key = env["key"]
            env_type = env["type"]
            required = env["required"]
            default_value = env["default_value"]

            try:
                value = os.environ[key.value[0]]

                if len(value) == 0:
                    raise KeyError

                if env_type == int:
                    self._environments[key] = int(value)
                elif env_type == float:
                    self._environments[key] = float(value)
                elif env_type == bool:
                    self._environments[key] = value in ["true", "True", "1"]
                else:
                    self._environments[key] = value
            except KeyError:
                if required is True:
                    raise EnvironmentNotProvided("Environment '{}' was not provided".format(key))
                else:
                    self._environments[key] = default_value
            except ValueError:
                raise InvalidEnvironment("The value of environment '{}' is invalid".format(key))

    def get(self, key):
        if type(key) == str:
            key = EnvKeys[key]

        return self._environments[key]

    def set(self, key, value):
        if type(key) == str:
            key = EnvKeys[key]

        self._environments[key] = value


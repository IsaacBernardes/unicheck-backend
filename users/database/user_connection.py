import os
import psycopg2

__creator__ = "IsaacBernardes"
__last_modifier__ = "IsaacBernardes"
__last_modify__ = "05/09/2022"
__version__ = open("version").read()


class UserConnection:
    def __init__(self):
        self.host = os.environ['DB_HOST']
        self.port = os.environ['DB_PORT']
        self.user = os.environ['DB_USER']
        self.password = os.environ['DB_PASS']
        self.database = os.environ['DB_NAME']

    def init_connection(self) -> psycopg2._psycopg.connection:
        return psycopg2.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            dbname=self.database
        )

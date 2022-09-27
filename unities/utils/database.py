import psycopg2

from utils.environments import Environment, EnvKeys

__creator__ = "IsaacBernardes"
__last_modifier__ = "IsaacBernardes"
__last_modify__ = "05/09/2022"
__version__ = open("version").read()


class Connection:
    def __init__(self):
        environ = Environment()
        self.host = environ.get(EnvKeys.DB_HOST)
        self.port = environ.get(EnvKeys.DB_PORT)
        self.user = environ.get(EnvKeys.DB_USER)
        self.password = environ.get(EnvKeys.DB_PASS)
        self.database = environ.get(EnvKeys.DB_NAME)

    def init_connection(self) -> psycopg2._psycopg.connection:
        return psycopg2.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            dbname=self.database
        )

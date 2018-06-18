import os
import psycopg2
from configparser import ConfigParser
from utils.snaql_queries import queries, exec_query


def get_configuration():
    conf = ConfigParser()
    conf.read(os.path.dirname(__file__) + '/config.ini')
    return conf


def get_db_connection(db_server: str = 'redshift'):
    conf = get_configuration()
    return DatabaseAccessClient(user=conf[db_server]['user'],
                                password=conf[db_server]['password'],
                                host=conf[db_server]['host'],
                                port=conf[db_server]['port'],
                                dbname=conf[db_server]['dbname'],
                                sslmode=conf[db_server]['sslmode'],
                                sslrootcert=conf[db_server]['sslrootcert'])


class DatabaseAccessClient:
    def __init__(self, user: str, password: str, host: str, port: str, dbname: str, sslmode: str, sslrootcert: str):
        self._user = user
        self._password = password
        self._host = host
        self._port = port
        self._dbname = dbname
        self._sslmode = sslmode
        self._sslrootcert = sslrootcert
        self._conn = None

    def connect(self):
        try:
            self._conn = psycopg2.connect(host=self._host, port=self._port, user=self._user, password=self._password,
                                          dbname=self._dbname, sslmode=self._sslmode, sslrootcert=self._sslrootcert)
        except psycopg2.Error:
            raise RuntimeError("Unable to connect {}!".format(self._host))

    def get_conn(self):
        return self._conn

    def close(self):
        if self._conn:
            self._conn.close()


def get_creative_text(db_conn, creativeid):
    params = {'creativeid': creativeid}
    result = exec_query(db_conn, queries.get_creative_text(), params)
    if len(result) > 0:
        return result[0]['text']
    else:
        raise RuntimeError("Creative ID {} not existing".format(creativeid))

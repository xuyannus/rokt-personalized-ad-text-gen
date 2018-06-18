import os
from snaql.factory import Snaql
from psycopg2.extras import DictCursor

snaql_factory = Snaql(os.path.dirname(__file__), "./")

queries = snaql_factory.load_queries('queries.sql')


def exec_query(conn, sql, params=None):
    with conn.cursor(cursor_factory=DictCursor) as cur:
        cur.execute(sql, params)
        return cur.fetchall()

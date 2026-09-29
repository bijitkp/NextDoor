import psycopg

from config.config import settings


class Database:

    def __init__(self, database_name: str):
        self.database_name = database_name

    def _get_connection(self):
        return psycopg.connect(
            host=settings.postgres_host,
            port=settings.postgres_port,
            dbname=self.database_name,
            user=settings.postgres_admin_user,
            password=settings.postgres_admin_password,
        )

    def execute(self, query: str, params=None):
        with self._get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, params)

    def fetch_one(self, query: str, params=None):
        with self._get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchone()

    def fetch_all(self, query: str, params=None):
        with self._get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()
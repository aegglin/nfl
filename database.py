import pandas as pd
import sqlalchemy as sa


class Database:
    def __init__(self, server, database, username=None, password=None):
        self._sa_create_engine(server, database, username, password)

    def _sa_create_engine(self, server, database, username=None, password=None):
        driver = "ODBC Driver 18 for SQL Server"
        driver = driver.replace(" ", "+")

        base_url = (
            f"mssql+pyodbc://{server}/{database}?driver={driver}&trusted_connection=yes"
        )

        self._engine = sa.create_engine(base_url, fast_executemany=True)

    def execute(self, statement):
        with self._engine.connect() as connection:
            with connection.begin():
                query = sa.text(statement)
                connection.execution_options(autocommit=True).execute(query)
        connection.close()

    def query(self, statement):
        with self._engine.connect() as connection:
            query = sa.text(statement)
            data = pd.read_sql(query, connection)

        return data

    def read_table(self, obj):
        return self.query(f"SELECT * FROM {obj}")

    def write_table(self, obj, data):
        if "." not in obj:
            schema = "dbo"
            table = obj
        else:
            schema, table = obj.split(".")

        with self._engine.begin():
            data.to_sql(
                table, self._engine, schema=schema, index=False, if_exists="append"
            )

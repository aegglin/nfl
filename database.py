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

        sa.create_engine(base_url, fast_executemany=True)

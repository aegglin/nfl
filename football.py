from database import Database


class Football(Database):
    def __init__(self):
        server = "DESKTOP-D37151K\SQLEXPRESS"
        database = "Football"

        super().__init__(server, database)

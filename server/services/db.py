import sqlite3
import pandas as pd
import os

from server.settings import DB_PATH


class Database:

    def __init__(self, db_path):
        self.path = db_path
        self.con = sqlite3.connect(self.path)

    @classmethod
    def from_default_path(cls):
        return cls(DB_PATH)

    def fetch(self, sql):
        return pd.read_sql(sql, self.con)

    def import_csv_files_from_dir(self, dir_name):
        csv_files = [
            os.path.join(dir_name, foo)
            for foo
            in os.listdir(dir_name) if foo.endswith(".csv")]

        for csv_file in csv_files:
            self.create_table_by_csv_file(csv_file)

    def create_table_by_csv_file(self, file_path):
        table_name = os.path.basename(file_path).split(".")[0]
        df = pd.read_csv(file_path)
        print(f"Creating table: {table_name}")
        return df.to_sql(table_name, self.con, if_exists="replace")

    def __del__(self):
        self.con.close()

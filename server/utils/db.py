# -*- coding: utf-8 -*-
import logging
import sqlite3
import pandas as pd
import os

from settings import DB_PATH, DATA_DIR
from utils.logger import get_logger


class Database:
    def __init__(self, db_path):
        self._path = db_path
        self._con = sqlite3.connect(self._path)
        self._logger = get_logger(
            f"Database({os.path.basename(self._path)})",
            stdout_level=logging.DEBUG,
            file_level=logging.DEBUG,
        )

    @classmethod
    def from_default_path(cls):
        return cls(DB_PATH)

    def fetch(self, sql: str) -> pd.DataFrame:
        """
        Fetch data from the database
        :param sql: The SQL query
        :return: The data as a pandas dataframe
        """
        return pd.read_sql(sql, self._con)

    def import_csv_files_from_dir(self, dir_name):
        """
        Import all csv files from a directory into the database
        :param dir_name: The directory name
        """
        csv_files = [
            os.path.join(dir_name, foo)
            for foo in os.listdir(dir_name)
            if foo.endswith(".csv")
        ]

        for csv_file in csv_files:
            self.create_table_by_csv_file(csv_file)

    def create_table_by_csv_file(self, file_path: str):
        """
        Create a table in the database from a csv file
        :param file_path: The path to the csv file
        """
        table_name = os.path.basename(file_path).split(".")[0]
        df = pd.read_csv(file_path)
        self._logger.debug(f"Creating table: {table_name}")
        df.to_sql(table_name, self._con, if_exists="replace")

    def __del__(self):
        self._con.close()


Database.from_default_path().import_csv_files_from_dir(DATA_DIR)

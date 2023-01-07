# -*- coding: utf-8 -*-
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGS_DIR = os.path.join(BASE_DIR, "logs")
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(BASE_DIR, "db.sqlite3")

SERVER_PORT = os.getenv("PORT", 8000)
SERVER_DEBUG = False  # os.getenv("DEBUG", "True").lower() == "true"

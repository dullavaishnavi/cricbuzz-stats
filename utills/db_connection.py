import sqlite3
import pandas as pd

DB_FILE = "cricbuzz_stats.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def run_query(query, params=None):
    conn = get_connection()
    if params:
        df = pd.read_sql(query, conn, params=params)
    else:
        df = pd.read_sql(query, conn)
    conn.close()
    return df

def execute_dml(query, params=None):
    conn = get_connection()
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    conn.commit()
    conn.close()

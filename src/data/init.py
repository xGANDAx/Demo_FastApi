"""
Module that initializes the database.
"""

import os
from sqlite3 import connect, Connection, Cursor

conn: Connection | None = None
curs: Cursor | None = None


def get_db(name: str | None = None, reset: bool = False):
    """
    Function that initializes the database.
    """

    global conn, curs
    if conn:
        if not reset:
            return
        conn = None
    if not name:
        name = os.getenv("CRYPTID_SQLITE_DB", ":memory:")

    conn = connect(name, check_same_thread=False)
    curs = conn.cursor()


get_db()

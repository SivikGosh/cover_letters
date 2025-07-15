from sqlite3 import connect
from typing import Optional, Tuple, cast


def create_database(user_id: int) -> None:
    with connect(f'{user_id}.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS letters (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT UNIQUE NOT NULL,
                text TEXT NOT NULL
            );
            """
        )


def add_letter(user_id: int, title: str, text: str) -> None:
    with connect(f'{user_id}.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO letters ( title, text ) VALUES ( ?, ? );
            """, (title, text)
        )


def get_letter(user_id: int) -> Optional[Tuple[int, str, str]]:
    with connect(f'{user_id}.db') as connection:
        cursor = connection.cursor()
        query = cursor.execute("SELECT * FROM letters;")
        letter = query.fetchone()
        if letter is None:
            return None
        return cast(Tuple[int, str, str], letter)

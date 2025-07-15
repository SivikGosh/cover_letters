from sqlite3 import connect


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


def add_letter(user_id: str, title: str, text: str) -> None:
    with connect(f'{user_id}.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO letters ( title, text ) VALUES ( ?, ? );
            """, (title, text)
        )

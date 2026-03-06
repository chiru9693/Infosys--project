import sqlite3

def create_table(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            score INTEGER NOT NULL,
            sentiment TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def insert_bulk(db_name, records):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.executemany("""
        INSERT INTO results (text, score, sentiment)
        VALUES (?, ?, ?)
    """, records)

    conn.commit()
    conn.close()


def fetch_summary(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT sentiment, COUNT(*)
        FROM results
        GROUP BY sentiment
    """)

    data = cursor.fetchall()
    conn.close()
    return data


def search_by_sentiment(db_name, sentiment_type):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT text, score
        FROM results
        WHERE sentiment = ?
        LIMIT 5
    """, (sentiment_type,))

    data = cursor.fetchall()
    conn.close()
    return data
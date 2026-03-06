import sqlite3
import time


def create_table():
    conn = sqlite3.connect("reviews.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            review TEXT,
            sentiment TEXT,
            score INTEGER
        )
    """)

    conn.commit()
    conn.close()


def bulk_insert(data):
    conn = sqlite3.connect("reviews.db")
    cursor = conn.cursor()

    start = time.time()

    cursor.executemany(
        "INSERT INTO reviews (review, sentiment, score) VALUES (?, ?, ?)",
        data
    )

    conn.commit()
    insert_time = time.time() - start

    conn.close()
    return insert_time


def create_index():
    conn = sqlite3.connect("reviews.db")
    cursor = conn.cursor()

    cursor.execute("CREATE INDEX IF NOT EXISTS idx_sentiment ON reviews(sentiment)")
    conn.commit()
    conn.close()


def query_sentiment(sentiment):
    conn = sqlite3.connect("reviews.db")
    cursor = conn.cursor()

    start = time.time()
    cursor.execute("SELECT * FROM reviews WHERE sentiment=?", (sentiment,))
    rows = cursor.fetchall()
    query_time = time.time() - start

    conn.close()
    return len(rows), query_time
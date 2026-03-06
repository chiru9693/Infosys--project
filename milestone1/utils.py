import sqlite3
import csv

def export_to_csv(db_name, output_file="output.csv"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM results")
    rows = cursor.fetchall()

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Text", "Score", "Sentiment"])
        writer.writerows(rows)

    conn.close()

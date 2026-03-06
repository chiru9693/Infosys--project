from concurrent.futures import ThreadPoolExecutor
import time
import os

from text_generator import generate_file
from chunker import split_into_chunks
from sentiment import analyze_sentiment
from database import create_table, insert_bulk, fetch_summary

FILE_NAME = "sample.txt"
DB_NAME = "company.db"


def process_chunk(chunk):
    results = []
    for line in chunk:
        score, label = analyze_sentiment(line.strip())
        results.append((line.strip(), score, label))
    return results


def main():
    start_time = time.time()

    print("Step 1: Generating file...")
    generate_file(FILE_NAME, 1000)
    print("1000 lines generated.")

    print("Step 2: Creating chunks...")
    chunks = split_into_chunks(FILE_NAME, 100)
    print("Total Chunks:", len(chunks))
    print("Lines in First Chunk:", len(chunks[0]))

    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)

    create_table(DB_NAME)

    print("Step 3: Parallel processing started...")

    all_results = []

    with ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(process_chunk, chunks)
        for r in results:
            all_results.extend(r)

    print("Total Records Processed:", len(all_results))

    insert_bulk(DB_NAME, all_results)

    print("\nSentiment Summary:")
    for row in fetch_summary(DB_NAME):
        print(row)

    end_time = time.time()
    print(f"\nExecution Time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()
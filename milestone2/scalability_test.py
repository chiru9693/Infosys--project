from generate_reviews import generate_reviews
from performance import single_processing
from database import bulk_insert, query_sentiment


def run_test(count):
    print(f"\nTesting with {count} reviews")

    reviews = generate_reviews(count)

    results, processing_time = single_processing(reviews)
    insert_time = bulk_insert(results)
    _, query_time = query_sentiment("Positive")

    print(f"Processing Time: {processing_time:.2f} sec")
    print(f"Insert Time: {insert_time:.2f} sec")
    print(f"Query Time: {query_time:.2f} sec")
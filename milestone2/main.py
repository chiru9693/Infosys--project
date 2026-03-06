from generate_reviews import generate_reviews
from performance import single_processing, thread_processing, multiprocessing_processing
from database import create_table, bulk_insert, create_index, query_sentiment


if __name__ == "__main__":

    create_table()

    dataset_sizes = [50000, 100000, 1000000]

    for size in dataset_sizes:

        print("\n===================================")
        print(f"   SENTIMENT ANALYSIS REPORT ({size} Reviews)")
        print("===================================\n")

        reviews = generate_reviews(size)

        # -----------------------------
        # Performance Comparison
        # -----------------------------
        single_results, single_time = single_processing(reviews)
        thread_results, thread_time = thread_processing(reviews)
        mp_results, mp_time = multiprocessing_processing(reviews)

        print("Performance Comparison:")
        print("-----------------------------------")
        print(f"Single Processing       : {single_time:.4f} sec")
        print(f"Thread Processing       : {thread_time:.4f} sec")
        print(f"Multiprocessing         : {mp_time:.4f} sec")

        times = {
            "Single": single_time,
            "Thread": thread_time,
            "Multiprocessing": mp_time
        }

        fastest = min(times, key=times.get)

        print(f"Fastest Method          : {fastest}")

        # -----------------------------
        # Sentiment Distribution
        # -----------------------------
        total = len(single_results)

        positive = sum(1 for r in single_results if r[1] == "Positive")
        negative = sum(1 for r in single_results if r[1] == "Negative")
        neutral = sum(1 for r in single_results if r[1] == "Neutral")

        print("\nSentiment Distribution:")
        print("-----------------------------------")
        print(f"Positive : {positive} ({positive/total*100:.1f}%)")
        print(f"Negative : {negative} ({negative/total*100:.1f}%)")
        print(f"Neutral  : {neutral} ({neutral/total*100:.1f}%)")

        # -----------------------------
        # Database Performance
        # -----------------------------
        insert_time = bulk_insert(single_results)

        print("\nDatabase Performance:")
        print("-----------------------------------")
        print(f"Bulk Insert Time        : {insert_time:.4f} sec")

        _, before_time = query_sentiment("Positive")

        create_index()

        _, after_time = query_sentiment("Positive")

        improvement = ((before_time - after_time) / before_time) * 100

        print(f"Query Before Index      : {before_time:.4f} sec")
        print(f"Query After Index       : {after_time:.4f} sec")
        print(f"Index Improvement       : {improvement:.2f}% Faster")

        # -----------------------------
        # Performance Analysis
        # -----------------------------
        if improvement > 0:
            print("Index improves query performance.")
        else:
            print("Index has minimal impact for this dataset size.")

        print("\nScalability Observation:")
        print("-----------------------------------")
        print("Processing time increases as dataset grows.")
        print("Multiprocessing becomes more beneficial for large datasets.")
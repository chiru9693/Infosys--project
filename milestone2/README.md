Sentiment Analysis System – Milestone 2
📌 Overview

This project implements a Weighted Rule-Based Sentiment Analysis System.

It:

Calculates sentiment score using word weights

Classifies reviews as Positive, Negative, or Neutral

Compares performance (Single vs Threading vs Multiprocessing)

Stores results in SQLite database

Applies database optimization techniques

⚙ Sentiment Logic

Each word has a weight.

Example:

positive_rules = {"excellent": 3, "amazing": 2, "good": 1}
negative_rules = {"terrible": -3, "bad": -1, "error": -2}

Score Rules:

Score > 0 → Positive

Score < 0 → Negative

Score = 0 → Neutral

🚀 Performance Comparison

Tested using:

Single Processing (for-loop)

ThreadPoolExecutor

Multiprocessing Pool

Execution time is measured and compared.

📊 Scalability Testing

Tested with:

100 reviews

10,000 reviews

100,000 reviews

Observation:

Processing time increases with data size

Multiprocessing performs better for large datasets

🗄 Database Optimization

Implemented:

Bulk Insert using executemany()

Index creation:

CREATE INDEX idx_sentiment ON reviews(sentiment);

Index improves query performance.


🧠 Concepts Covered

Weighted sentiment scoring

CPU-bound vs I/O-bound

Global Interpreter Lock (GIL)

Multithreading vs Multiprocessing

SQLite optimization

Scalability analysis

//Over All Result//
===================================
   SENTIMENT ANALYSIS REPORT (50000 Reviews)
===================================

Performance Comparison:
-----------------------------------
Single Processing       : 1.0670 sec
Thread Processing       : 1.3830 sec
Multiprocessing         : 1.2316 sec
Fastest Method          : Single

Sentiment Distribution:
-----------------------------------
Positive : 25082 (50.2%)
Negative : 14889 (29.8%)
Neutral  : 10029 (20.1%)

Database Performance:
-----------------------------------
Bulk Insert Time        : 0.1830 sec
Query Before Index      : 15.5742 sec
Query After Index       : 3.6006 sec
Index Improvement       : 76.88% Faster
Index improves query performance.

Scalability Observation:
-----------------------------------
Processing time increases as dataset grows.
Multiprocessing becomes more beneficial for large datasets.

===================================
   SENTIMENT ANALYSIS REPORT (100000 Reviews)
===================================

Performance Comparison:
-----------------------------------
Single Processing       : 1.7712 sec
Thread Processing       : 2.6917 sec
Multiprocessing         : 1.2098 sec
Fastest Method          : Multiprocessing

Sentiment Distribution:
-----------------------------------
Positive : 49655 (49.7%)
Negative : 30210 (30.2%)
Neutral  : 20135 (20.1%)

Database Performance:
-----------------------------------
Bulk Insert Time        : 0.2461 sec
Query Before Index      : 3.8571 sec
Query After Index       : 3.9974 sec
Index Improvement       : -3.64% Faster
Index has minimal impact for this dataset size.

Scalability Observation:
-----------------------------------
Processing time increases as dataset grows.
Multiprocessing becomes more beneficial for large datasets.

===================================
   SENTIMENT ANALYSIS REPORT (1000000 Reviews)
===================================

Performance Comparison:
-----------------------------------
Single Processing       : 18.4804 sec
Thread Processing       : 26.5257 sec
Multiprocessing         : 4.6583 sec
Fastest Method          : Multiprocessing

Sentiment Distribution:
-----------------------------------
Positive : 499898 (50.0%)
Negative : 299701 (30.0%)
Neutral  : 200401 (20.0%)

Database Performance:
-----------------------------------
Bulk Insert Time        : 1.9574 sec
Query Before Index      : 4.3048 sec
Query After Index       : 4.1841 sec
Index Improvement       : 2.80% Faster
Index improves query performance.

Scalability Observation:
-----------------------------------
Processing time increases as dataset grows.
Multiprocessing becomes more beneficial for large datasets.
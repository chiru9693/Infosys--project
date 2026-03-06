import re
from collections import Counter

# Weighted sentiment dictionary
positive_rules = {
    "excellent": 3,
    "amazing": 3,
    "great": 2,
    "good": 1,
    "happy": 2,
    "love": 3,
    "nice": 1,
    "fantastic": 3
}

negative_rules = {
    "terrible": -3,
    "bad": -1,
    "worst": -3,
    "error": -2,
    "hate": -3,
    "poor": -2,
    "slow": -1,
    "problem": -2
}


# ----------------------------
# Text Preprocessing
# ----------------------------
def preprocess_text(text):
    """
    Basic NLP preprocessing
    - Lowercase
    - Remove punctuation
    - Tokenize
    """

    text = text.lower()

    # remove punctuation
    text = re.sub(r"[^\w\s]", "", text)

    # tokenize
    tokens = text.split()

    return tokens


# ----------------------------
# Feature Extraction
# ----------------------------
def extract_features(tokens):
    """
    Creates word frequency features
    Useful for larger NLP style processing
    """

    word_counts = Counter(tokens)

    return word_counts


# ----------------------------
# Sentiment Scoring
# ----------------------------
def compute_score(word_counts):
    """
    Weighted scoring algorithm
    """

    score = 0

    for word, count in word_counts.items():

        if word in positive_rules:
            score += positive_rules[word] * count

        if word in negative_rules:
            score += negative_rules[word] * count

    return score


# ----------------------------
# Sentiment Classification
# ----------------------------
def classify(score):

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"


# ----------------------------
# Main Sentiment Function
# ----------------------------
def analyze_sentiment(review):

    # Step 1: Preprocess text
    tokens = preprocess_text(review)

    # Step 2: Extract features
    word_counts = extract_features(tokens)

    # Step 3: Simulate heavier NLP workload
    score = 0
    for _ in range(50):
        score += compute_score(word_counts)

    # Step 4: Classification
    sentiment = classify(score)

    return (review, sentiment, score)
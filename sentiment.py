import string

positive_words = {"good", "great", "excellent", "happy", "love", "nice"}
negative_words = {"bad", "poor", "sad", "hate", "terrible", "worst"}

def analyze_sentiment(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()

    score = 0

    for word in words:
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1

    if score > 0:
        sentiment = "Positive"
    elif score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return score, sentiment
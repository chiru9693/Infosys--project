import random

sample_reviews = [
    "This product is amazing",
    "The service was terrible",
    "Excellent quality and good support",
    "Worst experience ever",
    "I am very happy",
    "Bad packaging but good product",
    "This is amazing but has error",
    "Absolutely excellent performance",
    "Not good not bad",
    "Terrible customer service"
]

def generate_reviews(count):
    return [random.choice(sample_reviews) for _ in range(count)]
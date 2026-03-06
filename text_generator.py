import random

sentences = [
    "I love this product it is excellent",
    "This is the worst experience ever",
    "The service is good and nice",
    "I hate this terrible thing",
    "It is an average day",
    "What a great performance",
    "This is bad and poor quality"
]

def generate_file(filename, lines):
    with open(filename, "w") as f:
        for _ in range(lines):
            f.write(random.choice(sentences) + "\n")
import re
from collections import Counter

reviews = [
    "Great product, battery life is excellent and durable.",
    "Very bad customer support and slow shipping.",
    "Excellent quality product, highly recommend this product.",
    "Fast delivery, good packaging, battery life is good.",
    "Affordable price and great features overall."
]

all_text = " ".join(reviews).lower()
words = re.findall(r'\b\w+\b', all_text)
freq = Counter(words)

print("Customer Reviews Word Frequency Distribution:")
for word, count in freq.most_common(12):
    print(f"{word:<12}: {count}")

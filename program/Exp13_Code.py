import re
from collections import Counter

filename = "sample_text.txt"
try:
    with open(filename, "r") as file:
        text = file.read().lower()
except FileNotFoundError:
    text = "Data science is an interdisciplinary field that uses data to extract insights."

words = re.findall(r'\b\w+\b', text)
freq = Counter(words)

print(f"Total Words Counted: {len(words)}")
print(f"Unique Words Counted: {len(freq)}")
print("\nWord Frequency Distribution (Top 10):")
for word, count in freq.most_common(10):
    print(f"{word}: {count}")

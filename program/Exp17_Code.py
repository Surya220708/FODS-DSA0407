import re
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

stopwords = set(['the', 'and', 'is', 'to', 'a', 'of', 'in', 'was', 'very', 'all'])

df = pd.read_csv("data.csv")
all_feedback = " ".join(df['feedback'].dropna()).lower()
words = re.findall(r'\b\w+\b', all_feedback)
filtered_words = [w for w in words if w not in stopwords]

freq = Counter(filtered_words)
n = 5
top_n = freq.most_common(n)

print(f"Top {n} Most Frequent Words:")
for word, count in top_n:
    print(f"{word}: {count}")

words_plot, counts_plot = zip(*top_n)
plt.figure(figsize=(7, 4))
plt.bar(words_plot, counts_plot, color='teal')
plt.title(f"Top {n} Frequent Words in Customer Feedback")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.savefig("exp17_plot.png")
print("Bar graph of top words saved to exp17_plot.png.")

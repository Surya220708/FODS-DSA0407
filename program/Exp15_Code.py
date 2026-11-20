from collections import Counter

likes = [10, 25, 10, 50, 25, 10, 100, 50, 25, 15]
likes_freq = Counter(likes)

print("Likes Frequency Distribution:")
for like_count, posts in sorted(likes_freq.items()):
    print(f"{like_count} likes: {posts} post(s)")

total_likes = sum(likes)
print(f"\nTotal Likes across posts: {total_likes}")
print(f"Average Likes per post: {total_likes / len(likes):.1f}")

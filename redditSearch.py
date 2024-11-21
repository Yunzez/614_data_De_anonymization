import praw

reddit = praw.Reddit(
    client_id="kiHWiz4jZLG5q_e3-3UWaA",
    client_secret="EWsqHiQJXWqsoraEWSCZVMZJP-VYjA",
    user_agent="614demo"
)

print(reddit.read_only)
print(reddit.user.me())
# Output: False

subreddit = reddit.subreddit("Washington")
print(f"Visiting subreddit: {subreddit.display_name}")


# Fetch and print titles of the top 10 hot posts
for post in subreddit.hot(limit=10):
    print(f"Title: {post.title}")
    print(f"Upvotes: {post.score}")
    print(f"URL: {post.url}")
    print("-" * 40)

# Example: Fetch a user's posts
def get_user_activity(username):
    user = reddit.redditor(username)
    return [post for post in user.submissions.new(limit=100)]

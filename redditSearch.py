import praw
from datetime import datetime, timezone

# Configure PRAW with your credentials
reddit = praw.Reddit(
    client_id="kiHWiz4jZLG5q_e3-3UWaA",
    client_secret="EWsqHiQJXWqsoraEWSCZVMZJP-VYjA",
    user_agent="614demo"
)

# Define keywords to search for
keywords = ["out of state drivers license transfer", "Transfer out of state drivers license"]

# Dynamically build the search query
search_query = " OR ".join(keywords)  # Combine keywords with 'OR'

# Define the subreddit
subreddit_name = "Washington"
subreddit = reddit.subreddit(subreddit_name)

# Define the target date range
start_date = datetime(2023, 1, 1, tzinfo=timezone.utc)
end_date = datetime(2025, 1, 1, tzinfo=timezone.utc)

# Fetch and process search results
matching_posts = []
search_results = subreddit.search(query=search_query, sort="new", time_filter="all")  # Fetch all time results

for post in search_results:
    post_date = datetime.fromtimestamp(post.created_utc, tz=timezone.utc)

    # Filter posts by the date range (2023 to 2024)
    if start_date <= post_date < end_date:
        matching_posts.append(post)

        # Fetch author details
        author = post.author  # Author object
        author_id = author.id if author else "N/A"  # Reddit ID of the author
        author_name = author.name if author else "Deleted"
        author_description = f"Redditor {author_name} (ID: {author_id})"

        print(f"Post Title: {post.title}")
        print(f"URL: {post.url}")
        print(f"Date: {post_date.strftime('%Y-%m-%d')}")
        print(f"Author: {author_description}")

        # Fetch comments in the post
        print("Comments by Author:")
        post.comments.replace_more(limit=0)  # Expand all comments
        for comment in post.comments:
            if comment.author and comment.author.name == author_name:  # Check if comment is by the author
                print(f"- Comment: {comment.body[:200]}")  # Print the first 200 characters of the comment
                print(f"  Date: {datetime.fromtimestamp(comment.created_utc, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')}")
                print("-" * 20)

        print("=" * 60)
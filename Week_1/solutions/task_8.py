# /// script
# dependencies = [
#   "requests",
# ]
# ///


import requests
import json
from dataclasses import dataclass

@dataclass
class Post:
    userId: int
    id: int
    title: str
    body: str

posts = []
# Decode the JSON response into a Post instance
for post_id in range(1, 4):  # Get posts 1-3
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    post_data = json.loads(response.content)
    
    post = Post(
        userId=post_data["userId"],
        id=post_data["id"],
        title=post_data["title"],
        body=post_data["body"]
    )
    posts.append(post)

# Display the posts
for i, post in enumerate(posts, 1):
    print(f"Post {i}:")
    print(f"    User ID: {post.userId}")
    print(f"    ID: {post.id}")
    print(f"    Title: {post.title}")
    print(f"    Body: {post.body}\n")
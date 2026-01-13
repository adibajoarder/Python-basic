from fastapi import FastAPI, HTTPException
from app.app import PostCreate
app = FastAPI()
text_posts = {1: "Hello World", 2: "FastAPI is great!", 3: "Python is awesome!"}

@app.get("/posts")
def get_posts(limit: int = None):
    if limit is not None:
        return list(text_posts.values())[:limit]
    return list(text_posts.values())


@app.get("/posts/{post_id}")
def get_post(post_id: int):
    if post_id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(post_id)

@app.post("/posts")
def create_post(post: PostCreate):
     new_post = {"title": post.title, "content": post.content}
     text_posts[max(text_posts.keys()) + 1] = new_post
     return new_post
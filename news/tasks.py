from develops_today_news.celery import app
from news.models import NewPost


@app.task
def reset_upvotes():
    post_list = NewPost.objects.all()
    for post in post_list:
        post.upvotes_amount = 0
        post.save()
        print(f"Successfully reset upvotes {post.id}")

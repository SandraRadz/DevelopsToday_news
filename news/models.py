from django.db import models


class NewPost(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    upvotes_amount = models.IntegerField(default=0)
    author_name = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author_name = models.CharField(max_length=255)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(NewPost, related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return "comment by " + self.author_name + " about " + self.post.title

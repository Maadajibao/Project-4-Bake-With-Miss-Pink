from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

# Post, class for post attributes

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    new_recipe = models.SlugField(max_length=200, unique=True)
    baker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pastry_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)


# Comments, class for comment attributes

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)


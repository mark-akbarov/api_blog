from django.db import models
from django.contrib.auth.models import User
from comments.models import Comment


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()

    @property
    def comment_count(self):
        p = Post.objects.get(pk=self.pk)
        return p.comments.all().count()

    def __str__(self) -> str:
        return self.title
from django.db import models
from django.contrib.auth.models import User



class Comment(models.Model):
    post = models.ForeignKey(to='posts.Post', on_delete=models.CASCADE, related_name='comments',)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=280)

    def __str__(self) -> str:
        return f'Comment by {self.author} on {self.post}'

    def comment_count(self) -> int:
        return Comment.objects.get(post=self.post).count()

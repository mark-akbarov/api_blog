from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from posts.models import Post


class Review(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    star = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)

    def __str__(self) -> str:
        return f'Review by {self.author} on {self.post}'

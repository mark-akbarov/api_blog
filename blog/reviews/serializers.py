from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = ['author', 'title', 'body', 'star']
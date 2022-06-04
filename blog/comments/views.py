from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .serializers import CommentSerializer
from .models import Comment

class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_pk'])

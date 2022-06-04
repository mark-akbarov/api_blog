from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .models import Review
from .serializers import ReviewSerializer



class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminUser]
   
    def get_queryset(self):
        return Review.objects.filter(post_id=self.kwargs['post_pk'])


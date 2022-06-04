from rest_framework_nested import routers

from comments.views import CommentViewSet
from reviews.views import ReviewViewSet
from .views import PostViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet)

posts_router = routers.NestedDefaultRouter(router, 'posts', lookup='post')
posts_router.register('comments', CommentViewSet, basename='post-comments')
posts_router.register('reviews', ReviewViewSet, basename='post-reviews')


urlpatterns = router.urls + posts_router.urls

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from .views import (CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet,
                    UserViewSet)

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(
    'posts/(?P<post_id>\\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register('follow', FollowViewSet, basename='follows')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/session-auth/', include('rest_framework.urls')),
    path('v1/', include('djoser.urls')),
    path(
        'v1/jwt/create/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'v1/jwt/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path('v1/jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

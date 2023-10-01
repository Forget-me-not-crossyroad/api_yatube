from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, GroupViewSet, PostViewSet

app_name = 'api'


v1_router = DefaultRouter()
v1_router.register('posts', PostViewSet)
v1_router.register('groups', GroupViewSet)
# v1_router.register('posts/<int:pk>/comments', CommentViewSet, basename='comments')
v1_router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')

# router.register('owners', OwnerViewSet)
# router.register(r'mycats', LightCatViewSet)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('admin/', admin.site.urls),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.views import GroupViewSet, PostViewSet

# app_name = 'api'


# v1_router = DefaultRouter()
# v1_router.register('posts', PostViewSet)
# v1_router.register('groups', GroupViewSet)
# router.register('owners', OwnerViewSet)
# router.register(r'mycats', LightCatViewSet)

urlpatterns = [
    path('api/', include('api.urls')),
    # path('admin/', admin.site.urls),
    # path('/v1/api-token-auth/', views.obtain_auth_token),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )

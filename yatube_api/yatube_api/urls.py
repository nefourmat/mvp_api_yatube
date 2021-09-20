from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

import api.views

router = routers.DefaultRouter()
router.register(r'posts', api.views.PostViewSet, basename='posts')
router.register(r'groups', api.views.GroupViewSet, basename='groups')
router.register(r'posts/(?P<post_id>\d+)/comments', api.views.CommentViewSet,
                basename='comments')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/', include(router.urls)),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )

from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

import api.views

v1_router = routers.DefaultRouter()
v1_router.register(r'posts', api.views.PostViewSet, basename='posts')
v1_router.register(r'groups', api.views.GroupViewSet, basename='groups')
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   api.views.CommentViewSet, basename='comments')
urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(v1_router.urls)),
]

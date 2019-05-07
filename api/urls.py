from django.conf.urls import url, include
from rest_framework import routers
from api.views import UserViewSet,GroupViewSet
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups',GroupViewSet)





urlpatterns = [

    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    ]
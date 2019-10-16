from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from user import views as user_views

router = routers.DefaultRouter()
router.register(r'user', user_views.UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

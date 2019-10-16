from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from establishment import views

router = routers.DefaultRouter()
router.register(r'establishment', views.EstablishmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('', admin.site.urls),
    path('api/', include('establishment.urls')),
    path('api/', include('user.urls')),

]

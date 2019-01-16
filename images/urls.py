from django.urls import path, include
from rest_framework import routers

from .viewsets import ImageViewSet
from .views import home

router = routers.DefaultRouter()
router.register(r'images', ImageViewSet)


urlpatterns = [
    path('', include((router.urls))),
    path('home/', home, name='home')
]

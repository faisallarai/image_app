from django.urls import path, include

from images import views

app_name = 'images'

urlpatterns = [
    path('', views.ImageListCreateAPIView.as_view(), name='list'),
    path('<int:pk>/', views.ImageRetrieveUpdateDestroyAPIView.as_view(), name='detail'),
]

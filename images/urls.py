from django.urls import path, include

from images import views
from images.api import viewsets

urlpatterns = [
    path('', views.index, name='index'),
    path('images/', views.ImageList.as_view(), name='images'),
    path('image/<int:pk>', views.ImageDetail.as_view(), name='image-detail')
]

# Add URLConf for create, update, delete
urlpatterns += [
    path('image/create/', views.ImageCreate.as_view(), name='image-create'),
    path('image/<int:pk>/update/', views.ImageDetail.as_view(),
         name='image-update'),
    path('image/<int:pk>/delete/', views.ImageDelete.as_view(),
         name='image-delete')
]

# Add URLConf for api
urlpatterns += [
    path('api/', viewsets.ImageListCreateAPIView.as_view(), name='list'),
    path('api/<int:pk>',
         viewsets.ImageRetrieveUpdateDestroyAPIView.as_view(), name='detail'),
]

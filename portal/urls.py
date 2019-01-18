from django.urls import path, include

from portal import views

app_name = 'portal'

urlpatterns = [
    path('', views.Index, name='index'),
    path('create/', views.Create, name='create'),
    path('<int:image_id>/update/', views.Update, name='update'),
]

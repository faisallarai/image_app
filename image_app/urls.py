from django.urls import path, include
from django.contrib import admin
from images import views


api_urls = [
    path('images/', include('images.urls'))
]

app_urls = [
    path('portal/', include('portal.urls'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
    path('portal/', include(app_urls)),
]

from django.conf.urls import include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('chat/', include('secureChat.urls')),
    path('api/', include('secureChat.urls')),
    path('user/', include('userControl.urls')),
    path('admin/', admin.site.urls),
    path('', include('secureChat.urls')),



]

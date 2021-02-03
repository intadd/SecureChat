from django.conf.urls import include, handler400,handler403,handler404, handler500
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('api/', include('secureChat.urls')),
    path('user/', include('userControl.urls')),
    path('admin/', admin.site.urls),
    path('', include('secureChat.urls')),
]

handler400 = 'secureChat.views.error400'
handler403 = 'secureChat.views.error403'
handler404 = 'secureChat.views.error404'
handler404 = 'secureChat.views.error500'




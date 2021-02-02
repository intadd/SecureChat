from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('server/',views.apiCreateServer,name='create'),
    path('<str:room_name>/', views.room, name='room'),
]

# chat/urls.py
from django.urls import path

from . import views
#from chats.views import index, chatPage

urlpatterns = [
    path('', views.index, name='home'),
    path('chat/<str:username>/', views.chatPage, name='chat'),
    #path('', views.index, name='index'),
    #path('<str:room_name>/', views.room, name='room'),
]

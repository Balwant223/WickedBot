from django.urls import path
from . import views
app_name = 'chat'
urlpatterns = [
    path('room/', views.chat_room,name='chat_room'),
    path('calls/',views.joke_calls,name='total_joke'),
]
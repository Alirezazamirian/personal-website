from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatroom, name='chatroom'),
    path("<str:room_name>/", views.room, name="room"),
]

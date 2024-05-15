from django.shortcuts import render


def chatroom(request):
    return render(request, 'chatapp/index.html', {})


def room(request, room_name):
    return render(request, "chatapp/room.html", {"room_name": room_name})

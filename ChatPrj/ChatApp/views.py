from django.shortcuts import render, redirect
from .models import *


def CreateRoom(request):
    # Cette vue permet de créer une nouvelle room de chat ou de rediriger vers une salle existante
    # en fonction du nom de la salle ('room') soumis via un formulaire.

    if request.method == 'POST':
        username = request.POST['username']
        room = request.POST['room']

        try:
            get_room = Room.objects.get(room_name=room)
            return redirect('room', room_name=room, username=username)

        except Room.DoesNotExist:
            new_room = Room(room_name=room)
            new_room.save()
            return redirect('room', room_name=room, username=username)

    return render(request, 'index.html')


def MessageView(request, room_name, username):
    # Cette vue gère l'affichage et l'envoi de messages dans une salle de chat spécifique.

    get_room = Room.objects.get(room_name=room_name)

    if request.method == 'POST':
        message = request.POST['message']

        print(message)

        new_message = Message(room=get_room, sender=username, message=message)
        new_message.save()

    get_messages = Message.objects.filter(room=get_room)

    context = {
        "messages": get_messages,
        "user": username,
        "room_name": room_name,
    }
    return render(request, 'message.html', context)
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from ChatApp.models import *


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        """
        Gère la connexion WebSocket d'un utilisateur à une salle de chat spécifique.
        """
        # récupère le nom de la salle à partir de l'URL de la requête
        self.room_name = f"room_{self.scope['url_route']['kwargs']['room_name']}"
        # ajoute la connexion WebSocket de l'utilisateur à un groupe de cette salle.
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        # Accepte la connexion WebSocket et permet l'échange de messages en temps réel
        await self.accept()

    async def disconnect(self, close_code):
        """
        Gère la déconnexion d'un utilisateur d'une salle de chat.

        Cette méthode est appelée lorsqu'un utilisateur se déconnecte de la WebSocket.
        Elle retire la connexion WebSocket de l'utilisateur du groupe de la salle en utilisant
        `group_discard`, ce qui empêche l'utilisateur de recevoir des messages envoyés à cette salle.
        """
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        """
        Reçoit un message envoyé par un utilisateur via WebSocket.

        Cette méthode est appelée lorsqu'un message est envoyé à la WebSocket depuis le client.
        Le message est d'abord transformé en format JSON, puis il est envoyé à tous les membres
        du groupe de la salle via `group_send`. Cela permet de diffuser le message à tous les
        utilisateurs connectés à la même salle de chat.
        """
        text_data_json = json.loads(text_data)
        message = text_data_json

        event = {
            'type': 'send_message',
            'message': message,
        }
        await self.channel_layer.group_send(self.room_name, event)

    async def send_message(self, event):
        """
        Envoie un message à l'utilisateur via WebSocket.

        Cette méthode est appelée lorsqu'un événement de type 'send_message' est envoyé au groupe
        de la salle. Elle traite le message, l'enregistre, puis le renvoie à tous
        les utilisateurs connectés à la salle via WebSocket.
        """
        data = event['message']
        await self.create_message(data=data)
        response_data = {
            'sender': data['sender'],
            'message': data['message']
        }
        await self.send(text_data=json.dumps({'message': response_data}))

    @database_sync_to_async
    def create_message(self, data):
        """
        Crée et enregistre un nouveau message dans la base de données.

        Cette méthode est utilisée pour enregistrer un message envoyé dans une salle de chat
        dans la base de données. Elle vérifie d'abord si le message existe déjà dans la salle
        puis crée un nouvel objet `Message` avec les données fournies et l'enregistre dans la base de données.
        """
        get_room_by_name = Room.objects.get(room_name=data['room_name'])
        if not Message.objects.filter(message=data['message']).exists():
            new_message = Message(room=get_room_by_name, sender=data['sender'], message=data['message'])
            new_message.save()
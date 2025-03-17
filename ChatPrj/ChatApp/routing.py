from django.urls import path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    #  Définit l'URL pour la connexion WebSocket à la salle de chat.
    # Lorsque l'utilisateur se connecte à 'ws/notification/<room_name>/',
    # la vue 'ChatConsumer' gère la connexion et la communication en temps réel pour cette salle.

    path('ws/notification/<str:room_name>/', ChatConsumer.as_asgi()),
]
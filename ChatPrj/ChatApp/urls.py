from django.urls import path
from . import views

urlpatterns = [
    # Redirige vers la vue CreateRoom pour créer une nouvelle salle de chat
    path('', views.CreateRoom, name='create-room'),
    # Redirige vers la vue qui affiche les messages d'une salle spécifique
    path('<str:room_name>/<str:username>/', views.MessageView, name='room'),
]
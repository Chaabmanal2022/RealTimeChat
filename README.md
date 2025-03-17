# RealTimeChat - Chat en temps réel avec Django et Channels

## Description
RealTimeChat est une application de chat en temps réel développée avec **Django** et **Channels**. 
Ce projet permet aux utilisateurs de discuter dans des "rooms" de chat via WebSocket. Les utilisateurs peuvent se connecter, envoyer des messages instantanément, et voir les messages des autres utilisateurs en temps réel sans recharger la page.

Ce projet utilise **Django Channels** pour gérer les connexions WebSocket et permettre une communication en temps réel entre les utilisateurs, tout en s'appuyant sur **Django** pour la gestion du back-end.

## Fonctionnalités
- Chat en temps réel avec WebSocket.
- Connexion à des "rooms" de chat.
- Interface utilisateur simple pour envoyer et recevoir des messages.
- Affichage des messages envoyés avec les horaires.
- Intégration de Django Admin pour la gestion des utilisateurs et des rooms.

## Prérequis
Avant de commencer, vous devez avoir **Python** et **pip** installés sur votre machine. Vous pouvez vérifier si vous les avez en exécutant les commandes suivantes :

```bash
python --version
pip --version
pip install channels
pip install daphne


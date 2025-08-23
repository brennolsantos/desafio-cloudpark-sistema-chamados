import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChamadoConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        pass
import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class ChamadoConsumer(WebsocketConsumer):
    def connect(self):
        self.usuario = self.scope["url_route"]["kwargs"]["username"]
        self.usuario_group_name = f"chamado_{self.usuario}"

        async_to_sync(self.channel_layer.group_add)(
            self.usuario_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.usuario_group_name, self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        async_to_sync(self.channel_layer.group_send)(
            self.usuario_group_name, {"type": "chamado.message", "message": message}
        )

    def chamado_message(self, event):
        message = event["message"]
        self.send(text_data=json.dumps({"message": message}))

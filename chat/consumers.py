import json
from .views import respond_to_websockets
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.utils import timezone

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = 'chat_%s' % self.id
        # join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
    # receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if 'user' in text_data_json:
            message=text_data_json['user']
            print(message)
            response=respond_to_websockets(message)
        else:
            message = text_data_json['message']
            response = respond_to_websockets(message)
        now = timezone.now()
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'sent_text':message,
                'message': response,
                'datetime': now.isoformat(),
            }
        )
    def chat_message(self, event):
        # Send message to WebSocket
        self.send(text_data=json.dumps(event))
    
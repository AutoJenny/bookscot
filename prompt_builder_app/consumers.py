import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings

class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json.get('action')

        if action == 'getDatabases':
            # Directly access the DATABASES setting
            database_names = list(settings.DATABASES.keys())
            
            await self.send(text_data=json.dumps({
                'type': 'databases',
                'payload': database_names
            }))

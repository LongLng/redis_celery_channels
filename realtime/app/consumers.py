from channels.generic.websocket import AsyncWebsocketConsumer

class JokesConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('app',self.channel_name)
        await self.accept()
        
    async def disconnect(self):
        await self.channel_layer.group_add('app',self.channel_name)
        
    async def send_jokes(self,event):
        text_massage = event['text']
        await self.send(text_massage)
import requests
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


channel_layer = get_channel_layer()

@shared_task
def get_joke():
    url = 'https://api.chucknorris.io/jokes/random'
    response =requests.get(url).json()
    realtime = response['value']
    async_to_sync(channel_layer.group_send)('app',{'type':'send_jokes','text':realtime})
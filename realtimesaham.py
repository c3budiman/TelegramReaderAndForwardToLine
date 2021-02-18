import asyncio
from telethon import events
import configparser
import json
# import asyncio
from datetime import date, datetime
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
    PeerChannel
)
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

# some functions to parse json date
class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        if isinstance(o, bytes):
            return list(o)
        return json.JSONEncoder.default(self, o)


# Reading Configs
config = configparser.ConfigParser()
config.read("config_saham.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

api_hash = str(api_hash)

phone = config['Telegram']['phone']
username = config['Telegram']['username']

line_access_token = config['Telegram']['line_access_token']
line_id = config['Telegram']['line_id']

# Create the client and connect
client = TelegramClient(username, api_id, api_hash)
#1452507073 Group GW
#1472431901 Group VIP
#1322999920 Channel VIP IDX
#1386278952 Channel VIP Binance
# https://web.telegram.org/#/im?p=c_4258021522888417678
# https://web.telegram.org/#/im?p=c_8003149890023288537
myChannelIDList = [1162942921,1276435477,1352550900]
line_bot_api = LineBotApi(line_access_token)
handlerwebhook = WebhookHandler(line_id)
whitelist=[
    'Uc677eb17c2b1274731dd6cc559116b45', #cecep budiman
    'Uedd4cfb6278f7e0b53947336b8e92630', #yaksa
    'U2b481aa1a6393cf608c7eba6ce95e4e5', #Handika
    'U66aa403f47e04f7e4e51f1057a0a32d8', #Yusuf
    'U291dcae373058be8bbd2a3a65ddfc516', #Ongki
]

@client.on(events.NewMessage(chats=myChannelIDList))
async def handler(event):
    # print(event.text)
    line_bot_api.multicast(whitelist, TextSendMessage(text=event.text))
    
client.start()
client.run_until_disconnected()
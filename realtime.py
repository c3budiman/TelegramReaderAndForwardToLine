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
config.read("config.ini")

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
#list of channel that you want to forward
myChannelIDList = [1,2,3]
line_bot_api = LineBotApi(line_access_token)
handlerwebhook = WebhookHandler(line_id)
#member that you want bot to forward the message to
whitelist=[
    'Uc677eb17c2b1274731dd6cc559116b45', #cecep budiman
]

@client.on(events.NewMessage(chats=myChannelIDList))
async def handler(event):
    # print(event.text)
    line_bot_api.multicast(whitelist, TextSendMessage(text=event.text))
    
client.start()
client.run_until_disconnected()

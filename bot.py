from telethon import TelegramClient, events
from datetime import datetime
import config

my_channel_id = -1000000000000
channels = [-1000000000001, -1000000000002]

client = TelegramClient('data', config.api_id, config.api_hash)
print("Resender started")


@client.on(events.NewMessage(chats=channels))
async def my_event_handler(event):
    chat = await event.get_chat()
    if event.message.media:
        await client.send_message(my_channel_id, event.message)
        print(datetime.strftime(datetime.now(), "%d.%m.%Y Re-sended at %H:%M:%S"), "from", chat.title)

client.start()
client.run_until_disconnected()

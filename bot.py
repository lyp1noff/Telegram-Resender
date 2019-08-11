from telethon import TelegramClient, events
import config

my_channel_id = -1001442545218
needed_channel_id = -1001423471875

client = TelegramClient('lyp1noff', config.api_id, config.api_hash)

print("Resender started")

@client.on(events.NewMessage(chats=needed_channel_id))
async def my_event_handler(event):
    if event:
        await client.send_message(my_channel_id, event.message)
        await print("Reposted")

client.start()
client.run_until_disconnected()

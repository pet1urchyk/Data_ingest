from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
import os
import logging
logging.basicConfig(format='[%(levelname)s %(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
session = os.getenv("SESSION_NAME")

client = TelegramClient(session,api_id,api_hash)
channel_link = "https://t.me/doucommunity"

async def join_channel(client,channel_link):
    try:
        await client(JoinChannelRequest(channel_link))
        print(f"Succesfully joined the chanel {channel_link}")
    except:
        print(f"Failed to join {channel_link}")

async def scrape(client, channel, limit=10):
    async for msg in client.iter_messages(channel,limit):
        if msg.text:
            print(msg.text)
        if msg.photo:
            path = await msg.download_media()
            print(f"Media saved to {path}")
    msg = await client.send_message("+48 453 577 441", "запуск")

@client.on(events.NewMessage)
async def answer(event):
    if "hello" in event.raw_text:
        await event.reply("hi!")

@client.on(events.NewMessage(outgoing=True, pattern=r'\.save'))
async def handler(event):
    if event.is_reply:
        replied = await event.get_reply_message()
        sender = replied.sender
        await client.download_profile_photo(sender)
        await event.respond('Saved your photo {}'.format(sender.username))

@client.on(events.NewMessage(pattern=r'(?i).*wtf'))
async def handler(event):
    await event.delete()

async def main():
    await join_channel(client, channel_link)

    await scrape(client,channel_link,2)

with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()
from telethon import TelegramClient, events
import os
import asyncio

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
session = os.getenv("SESSION_NAME")

client = TelegramClient(session,api_id,api_hash)
channel = "https://t.me/testDistributedMLSys"

POLL_INTERVAL = 5
WINDOW = 20  

async def poll(client,channel,limit=10):
    last_id = 0
    seen = {}
    while True:
        async for msg in client.iter_messages(channel, limit, min_id=last_id, reverse=True):
            last_id = msg.id
            seen[msg.id] = (msg.edit_date, msg.text)
            if msg.text:
                print(msg.text)
            if msg.photo:
                path = await msg.download_media()
                print(f"Media saved to {path}")

        async for msg in client.iter_messages(channel, limit=WINDOW):
            old = seen.get(msg.id)
            if old is not None and msg.edit_date != old[0]:
                print(f"edited id: {msg.id}: {old[1]} -> {msg.text}")
                seen[msg.id] = (msg.edit_date, msg.text)

        await asyncio.sleep(POLL_INTERVAL)
with client:
    try:
        client.loop.run_until_complete(poll(client,channel))
    except KeyboardInterrupt:
        print("Stopping")

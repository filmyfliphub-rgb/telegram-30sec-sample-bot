from pyrogram import Client, filters
import os
import subprocess

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client(
    "samplebot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.video | filters.audio)
async def sample_handler(client, message):
    msg = await message.reply("⏳ 30 sec sample bana raha hoon...")

    file_path = await message.download()
    output = "sample_30sec.mp4"

    subprocess.run([
        "ffmpeg", "-i", file_path,
        "-t", "30",
        "-c", "copy",
        output
    ])

    await message.reply_video(output, caption="🎬 30 Sec Sample")
    await msg.delete()

    os.remove(file_path)
    os.remove(output)

app.run()

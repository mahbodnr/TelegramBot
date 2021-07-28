import json

from Tbot.bot import TelegramBot
from Tbot.database import Database

with open('./secret.json') as f:
  secret = json.load(f)
  
bot = TelegramBot(
    secret['token'],
    database = Database(r"mongodb://localhost:27017/"),
    webhook = secret['webhook']
    )


@bot.onUpdate
async def show_message(update):
    if update.message:
        await bot.sendMessage(
            update.message._from.id,
            f"Hi {update.message._from.first_name}"
            )

# uvicorn app:bot.app --reload
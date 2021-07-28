import os
import json
import asyncio

from Tbot.bot import TelegramBot
from Tbot.database import Database
from Tbot.types import *


with open('./secret.json') as f:
  secret = json.load(f)
  
TOKEN = secret['token']

db = Database(r"mongodb://localhost:27017/")
bot = TelegramBot(
    TOKEN,
    database = db,
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
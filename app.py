import json

from pyngrok import ngrok


from Tbot.bot import TelegramBot
from Tbot.database import Database
from Tbot.filters import Filters, UpdateType

with open('./secret.json') as f:
  secret = json.load(f)

ngrok_webhook = ngrok.connect(addr = 8000, bind_tls=True).public_url

bot = TelegramBot(
    secret['token'],
    database = Database(r"mongodb://localhost:27017/"),
    webhook = ngrok.connect(addr = 8000, bind_tls=True).public_url #secret['webhook']
    )


@bot.onUpdate(filters= UpdateType(["edited_message", "message"]))
async def show_message(update):
    if update.message:
        await bot.sendMessage(
            update.message.from_.id,
            f"Hi {update.message.from_.first_name}"
            )
    elif update.edited_message:
        await bot.sendMessage(
          update.edited_message.from_.id,
          f"You edited your message. I am watching you 👀"
          )

# uvicorn app:bot.app --reload
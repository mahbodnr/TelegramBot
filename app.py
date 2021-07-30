import json

from pyngrok import ngrok


from Tbot.bot import TelegramBot
from Tbot.database import Database
from Tbot.filters import Filters, UpdateType
from Tbot.handlers import onUpdate, onMessage, onEditedMessage

with open('./secret.json') as f:
  secret = json.load(f)

ngrok_webhook = ngrok.connect(addr = 8000, bind_tls=True).public_url

bot = TelegramBot(
    secret['token'],
    database = Database(r"mongodb://localhost:27017/"),
    webhook = ngrok.connect(addr = 8000, bind_tls=True).public_url #secret['webhook']
    )

bot.listen()

@onUpdate
async def handle_updates(update):
    ...
    
@onMessage
async def handle_messages(message):
    await bot.sendMessage(
        message.from_.id,
        f"You said: {message.text}"
        )

@onEditedMessage
async def edit_message(edited_message):
    await bot.sendMessage(
      edited_message.from_.id,
      f"You edited your message. I am watching you 👀"
      )

# uvicorn app:bot.app --reload
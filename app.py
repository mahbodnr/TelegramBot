import json

from pyngrok import ngrok


from Tbot.bot import TelegramBot
from Tbot.database import Database
from Tbot.filters import FilterCollection, TargetChats
from Tbot.panels import AdminPanel

with open('./secret.json') as f:
  secret = json.load(f)

ngrok_webhook = ngrok.connect(addr = 8000, bind_tls=True).public_url

bot = TelegramBot(
    secret['token'],
    database = Database(r"mongodb://localhost:27017/"),
    webhook = ngrok.connect(addr = 8000, bind_tls=True).public_url #secret['webhook']
    )

bot.listen()
admin_panel = AdminPanel(bot)

@bot.onUpdate
@FilterCollection({TargetChats(secret['admin_chat_id'])})
async def handle_updates(update):
    await admin_panel(update)
    
@bot.onMessage
async def handle_messages(message):
    await bot.sendMessage(
        message.from_.id,
        f"You said: {message.text}"
        )

@bot.onMyChatMember
async def handle_my_chat_member(my_chat_member):
    await bot.sendMessage(
      my_chat_member.from_.id,
      str(my_chat_member.json())
      )

# uvicorn app:bot.app --reload
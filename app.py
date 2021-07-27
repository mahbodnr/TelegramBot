import os
import json
import asyncio

from bot import TelegramBot
from database import Database

from fastapi import FastAPI,Request

app = FastAPI()

with open('./secret.json') as f:
  secret = json.load(f)
TOKEN = secret['token']

db = Database(r"mongodb://localhost:27017/")
bot = TelegramBot(
    TOKEN,
    database = db,
    webhook = 'https://5c258255e65f.ngrok.io'
    )


@app.post("/")
async def recWebHook(req: Request):
    """
    Receive the Webhook and process the Webhook Payload to get relevant data
    """
    pm = await req.json()
    await bot.sendMessage(455572260, str(pm))

@app.get("/test")
async def test():
    return {"message": "Is working..."}

@app.get("/msg_test")
async def msg_test():
    msg = await bot.sendMessage(455572260, 'This message will be deleted :)')
    await bot.deleteMessage(msg.chat_id, msg.message_id)
    # return {"message": "Done"}

@app.get("/webhook_info")
async def webhook_info():
    info = await bot.getWebhookInfo()
    return info

@app.get("/set_webhook")
async def set_webhook():
    info = await bot.setWebhook(r'1743689155:AAGWsroVCMB3E9k6dgch9QZ-spwxto6GKuE')
    return info


import json
import asyncio

from bot import TelegramBot
from database import Database

async def main():
    db = Database(r"mongodb://localhost:27017/")
    bot = TelegramBot(
        r'1743689155:AAHeSu4jYeIgYMN5yOBVcb6RcHEXNV7-iJY',
        database = db,
        )
    msg = await bot.sendMessage(455572260, 'This message will be deleted :)')
    await bot.deleteMessage(msg.chat_id, msg.message_id)
    

if __name__ == '__main__':
    asyncio.run(main())
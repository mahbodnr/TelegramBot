import json
import asyncio

from bot import TelegramBot
from database import Database

async def main():
    mongodb_connection_info = json.load(open('./mongodb.json', 'r'))
    access_url= (
        "mongodb+srv://{}:{}@mahbodnr.z1box.mongodb.net/{}".format(
        mongodb_connection_info['user'], mongodb_connection_info['password'], "test_bot"
        )
        + "?retryWrites=true&w=majority"
    )
    db = Database(access_url)
    bot = TelegramBot(
        r'1743689155:AAHeSu4jYeIgYMN5yOBVcb6RcHEXNV7-iJY',
        database = db,
        )
    msg = await bot.sendMessage(455572260, 'This message will be deleted :)')
    print(msg.content)
    await bot.deleteMessage(msg.chat_id, msg.message_id)
    

if __name__ == '__main__':
    asyncio.run(main())
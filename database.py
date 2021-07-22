import pymongo
from pymongo import MongoClient

from message import TelegramMessage


class Database:
    def __init__(
        self,
        access_url,
        ):
        self.cluster = MongoClient(access_url)
        self.db = self.cluster['bot_db']
        self.users = self.db['users']
        self.messages = self.db['messages']


    def add_messages(
        self,
        msg: TelegramMessage,
        ):
        self.messages.insert_one(msg.content)


    def add_user(
        self,
        msg: TelegramMessage,
        ):
        self.messages.insert_one(
            {
                '_id': msg.chat_id,
                **msg.chat
            }
        )
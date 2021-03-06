
from pymongo import MongoClient
import httpx

from .types import Update, Message, User

class Database:
    def __init__(
        self,
        connecting_string: str = None,
        database_name = 'bot_db'
        ):
        self.cluster = MongoClient(connecting_string)
        self.db = self.cluster[database_name]
        # collections
        self.updates = self.db['updates']
        self.users = self.db['users']
        self.sent = self.db['sent']


    def add_update(self,
        update: Update,
        ):
        self.updates.insert_one(update.dict())


    def add_sent(
        self,
        response: httpx.Response,
        ):
        self.sent.insert_one(response.json())


    def add_user(
        self,
        user: User,
        ):
        if self.users.find({'_id':user.id}).count()>0:
            self.users.update_one(
                {'_id': user.id},
                {'$set': {**user.dict()}}
                )
        else:
            self.users.insert_one(
                {
                    '_id': user.id,
                    **user.dict(),
                }
            )
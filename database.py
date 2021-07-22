import pymongo
from pymongo import MongoClient

from message import TelegramMessage


class Database:
    def __init__(
        self,
        connecting_string: str,
        ):
        self.cluster = MongoClient(connecting_string)
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
        if db.messages.find({'_id':msg.chat_id}).count()>0:
            self.messages.update_one(
                {'_id':msg.chat_id},
                {'$set':{**msg.chat}}
                )
        else:
            self.messages.insert_one(
                {
                    '_id': msg.chat_id,
                    **msg.chat
                }
            )


if __name__ == '__main__':
    #test server
    import json
    mongodb_connection_info = json.load(open('./mongodb.json', 'r'))
    access_url= (
        "mongodb+srv://{}:{}@mahbodnr.z1box.mongodb.net/{}".format(
        mongodb_connection_info['user'], mongodb_connection_info['password'], "test_bot"
        )
        + "?retryWrites=true&w=majority"
    )
    db = Database(access_url)
    db.messages.update_one({'_id':1}, {'$set':{'value': 10}})
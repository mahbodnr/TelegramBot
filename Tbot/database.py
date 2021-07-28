from pymongo import MongoClient

from .message import TelegramMessage


class Database:
    def __init__(
        self,
        connecting_string: str = None,
        database_name = 'bot_db'
        ):
        self.cluster = MongoClient(connecting_string)
        self.db = self.cluster[database_name]
        self.users = self.db['users']
        self.messages = self.db['messages']


    def add_messages(
        self,
        msg: TelegramMessage,
        ):
        self.messages.insert_one(msg.result)


    def add_user(
        self,
        msg: TelegramMessage,
        ):
        if self.users.find({'_id':msg.chat_id}).count()>0:
            self.messages.update_one(
                {'_id':msg.chat_id},
                {'$set':{**msg.chat}}
                )
        else:
            self.users.insert_one(
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
    db = Database()
    db.messages.remove()
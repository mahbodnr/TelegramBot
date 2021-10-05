from typing import Union, List
from collections import Iterable 

from .filters import FilterCollection, FilterCondition
from .types import *

class Handler:
    def __init__(self,func):
        self.func = func
        self.handlers.add(func)

    def run(self, update):
        for func in self.handlers:
            func(update)


class onUpdate(Handler):
    """Response decorator for all Updates"""
    handlers = set()
    attr_name = 'update_id'
class onMessage(Handler):
    """Response decorator for Messages"""
    handlers = set()
    attr_name = 'message'

class onEditedMessage(Handler):
    """Response decorator for Edited Messages"""
    handlers = set()
    attr_name = 'edited_message'

class onMyChatMember(Handler):
    """Response decorator for Chat Members Activities"""
    handlers = set()
    attr_name = 'my_chat_member'


ALL_HANDLERS =[
    onUpdate,
    onMessage,
    onEditedMessage,
    onMyChatMember,
]
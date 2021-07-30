from typing import Union, List
from collections import Iterable 

from .filters import Filters, Filter
from .types import *

class Handler:
    def __init__(self,func):
        self.func = func
        self.handlers.add(func)

    def run(self, update):
        for func in self.handlers:
            func(update)


class onUpdate(Handler):
    handlers = set()


class onMessage(Handler):
    handlers = set()


class onEditedMessage(Handler):
    handlers = set()


from typing import Set, Callable, Union, List
from types import FunctionType

class FilterCondition:
    def __init__(self, pass_filter: Callable):
        self.pass_filter = pass_filter

    def __call__(self, update):
        return self.pass_filter(update)

    def __or__(self, other):
        assert isinstance(other, (FilterCondition, FilterCollection)), f"got {other} of type: {type(other)}"
        return FilterCollection({self, other}, operator = 'or')

    def __and__(self, other):
        assert isinstance(other, (FilterCondition, FilterCollection)), f"got {other} of type: {type(other)}"
        return FilterCollection({self, other}, operator = 'and')



class FilterCollection:
    def __init__(
        self,
        filters: Set["FilterCollection"],
        operator: str = None,
        ):
        self.filters_items = filters

        if len(self.filters_items) > 1:
            self.filters_items = set()
            for filters_item in filters:
                if isinstance(filters_item, FilterCondition):
                    self.filters_items.add(FilterCollection({filters_item}))
                elif isinstance(filters_item, FilterCollection):
                    self.filters_items.add(filters_item)
                elif isinstance(filters_item, FunctionType):
                    self.filters_items.add(FilterCollection({FilterCondition(filters_item)}))

                else:
                    raise ValueError(
                        "'filters_items' is a set of 'FunctionType', 'FilterCondition' or"
                        "'FilterCollection' instances."
                        f" got {filters_item} of type: {type(filters_item)}"
                        )
        self.operator = operator

    def __call__(self, func):
        @self.decorator
        def wrapped_func(*args):
            return func(*args)

        return wrapped_func
        

    def decorator(self, func):
        def decorator_function(*args):
            if self.check(args[0]):
                return func(*args)
            else:
                return self.do_nothing()
        return decorator_function

    async def do_nothing(self):
        ...

    def check(self, update):
        if len(self.filters_items) == 1:
            return next(iter(self.filters_items))(update)
        else:
            if self.operator == "and":
                for filters_item in self.filters_items:
                    if not filters_item.check(update):
                        return False
                return True
            elif self.operator == "or":
                for filters_item in self.filters_items:
                    if filters_item.check(update):
                        return True
                return False
            else:
                if self.operator is not None:
                    raise ValueError("operator must be either 'and' or 'or'.")

    def __or__(self, other):
        assert isinstance(other, (FilterCondition, FilterCollection)),(
        f"got {other} of type: {type(other)}"
        )
        return FilterCollection({self, other}, operator = 'or')

    def __and__(self, other):
        assert isinstance(other, (FilterCondition, FilterCollection)),(
        f"got {other} of type: {type(other)}"
        )
        return FilterCollection({self, other}, operator = 'and')


class TargetChats(FilterCondition):
    def __init__(
        self,
        chat_ids : Union[Set[int], int]
        ):
        if isinstance(chat_ids, (int, str)):
            self.chat_ids = {int(chat_ids)}
        else:
            self.chat_ids = {int(chat_id) for chat_id in chat_ids}

    def pass_filter(self, update):
        for message_type in { 
            "message",
            "edited_message",
            "channel_post",
            "edited_channel_post",
            "inline_query",
            "chosen_inline_result",
            "callback_query",
            "shipping_query",
            "pre_checkout_query",
            "poll",
            "poll_answer",
            "my_chat_member",
            "chat_member",
        }:
            if (
                getattr(update, message_type) and
                getattr(update, message_type).from_.id in self.chat_ids
            ):
                return True
        return False
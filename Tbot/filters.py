from typing import Set, Callable, Union, List


class Filter:
    def __init__(self, pass_filter: Callable):
        self.pass_filter = pass_filter

    def __call__(self, update):
        return self.pass_filter(update)

    def __or__(self, other):
        assert isinstance(other, (Filter, Filters)), f"got {other} of type: {type(other)}"
        return Filters({self, other}, operator = 'or')

    def __and__(self, other):
        assert isinstance(other, (Filter, Filters)), f"got {other} of type: {type(other)}"
        return Filters({self, other}, operator = 'and')



class Filters:
    def __init__(
        self,
        filters_items: Set["Filters"],
        operator: str = None,
        ):
        self.filters_items = filters_items

        if len(self.filters_items) > 1:
            self.filters_items = set()
            for filters_item in filters_items:
                if isinstance(filters_item, (Filter)):
                    self.filters_items.add(Filters({filters_item}))
                elif isinstance(filters_item, (Filters)):
                    self.filters_items.add(filters_item)
                else:
                    raise ValueError(
                        "'filters_items' is a set of 'Filter' or 'Filters' instances."
                        f" got {filters_item} of type: {type(filters_item)}"
                        )

        self.operator = operator


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
        assert isinstance(other, (Filter, Filters)), f"got {other} of type: {type(other)}"
        return Filters({self, other}, operator = 'or')

    def __and__(self, other):
        assert isinstance(other, (Filter, Filters)), f"got {other} of type: {type(other)}"
        return Filters({self, other}, operator = 'and')



class UpdateType(Filter):
    def __init__(self, update_type: Union[str, List[str]]):
        if type(update_type) == str:
            self.update_types = [update_type]
        elif type(update_type) == list:
            self.update_types = update_type
        else:
            raise ValueError(
                "update_type must be either a list or a string."
                f" got {update_type} of type: {type(update_type)}"
                )


    def pass_filter(self, update):
        for update_type in self.update_types:
            if getattr(update, update_type):
                return True,
        return False

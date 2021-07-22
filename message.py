import json
import requests

class TelegramMessage:
    def __init__(self,
        response: requests.Response
        ):
        self.response = response
        self.content = json.loads(response.content)
        self.ok = self.content['ok']
        self.result = self.content['result'] 
        if self.ok and type(self.result)==dict:
            self.set_attrs(self.content['result'])


    def set_attrs(self, dictionary, parent=None):
        for key, value in dictionary.items():
            if type(value) == dict:
                if parent:
                    setattr(self, f'{parent}_{key}', value)
                    new_parent = f'{parent}_{key}'
                else:
                    setattr(self, key, value)
                    new_parent = key
                self.set_attrs(value, parent=new_parent)
            else:
                if parent:
                    setattr(self, f'{parent}_{key}', value)
                else:
                    setattr(self, key, value)

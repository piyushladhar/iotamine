from .client import IotamineClient
from .vm import VM

class Iotamine:
    def __init__(self, api_key):
        self.client = IotamineClient(api_key)
        self.vm = VM(self.client)

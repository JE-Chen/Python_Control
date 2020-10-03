import keyboard
from Module.Abbreviation import Addreviation
from Module.Pressed import Pressed
from Module.HotKey import HotKey

class KeyboardCore():

    def __init__(self):
        self.Abbreviation=Addreviation()
        self.Pressed=Pressed
        self.HotKey=HotKey

    def write(self,writeString,delay=0,restore_state_after=True,exact=None):
        keyboard.write(writeString,delay,restore_state_after,exact)

    def send(self,sendString):
        keyboard.send(sendString)

    def unHookAll(self):
        keyboard.unhook_all()
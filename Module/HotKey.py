import keyboard

class HotKey():

    def __init__(self):
        pass

    def SetHotKey(self,hotKey,function):
        keyboard.add_hotkey(hotKey,lambda : function)

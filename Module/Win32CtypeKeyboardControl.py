import time
from Core.Util.Win32CtypeINPUT import *

class CtypeKeyboardControl():

    def PressKey(self, keyCode):
        x = INPUT(type=Keyboard,ki=KEYBDINPUT(wVk=keyCode))
        SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

    def ReleaseKey(self, keyCode):
        x = INPUT(type=Keyboard,ki=KEYBDINPUT(wVk=keyCode,dwFlags=EventF_KEYUP))
        SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def PressTest():
    keyboardControl = CtypeKeyboardControl()
    for i in range(10):
        keyboardControl.PressKey(key8)
        time.sleep(0.01)

if __name__ == "__main__":
    PressTest()
import time
from Core.Util.CtypeINPUT import *

class CtypeKeyboardControl():

    def PressKey(self, hexKeyCode):
        x = INPUT(type=Keyboard,ki=KEYBDINPUT(wVk=hexKeyCode))
        user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

    def ReleaseKey(self, hexKeyCode):
        x = INPUT(type=Keyboard,ki=KEYBDINPUT(wVk=hexKeyCode,dwFlags=EventF_KEYUP))
        user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


def PressTest():
    keyboardControl = CtypeKeyboardControl()
    for i in range(10):
        keyboardControl.PressKey(key8)
        #time.sleep(0.01)

if __name__ == "__main__":
    PressTest()

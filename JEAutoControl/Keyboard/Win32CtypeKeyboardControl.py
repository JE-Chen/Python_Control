from JEAutoControl.Core.Util.Win32CtypeINPUT import INPUT,Keyboard,KEYBDINPUT,SendInput,ctypes,EventF_KEYUP

def PressKey(keyCode):
    x = INPUT(type=Keyboard,ki=KEYBDINPUT(wVk=keyCode))
    SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def ReleaseKey(keyCode):
    x = INPUT(type=Keyboard,ki=KEYBDINPUT(wVk=keyCode,dwFlags=EventF_KEYUP))
    SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

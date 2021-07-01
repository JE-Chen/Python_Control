from je_auto_control.core.util.win32_ctype_input import Input,Keyboard,KeyboardInput,SendInput,ctypes,EventF_KEYUP

def PressKey(keyCode):
    x = Input(type=Keyboard, ki=KeyboardInput(wVk=keyCode))
    SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def ReleaseKey(keyCode):
    x = Input(type=Keyboard, ki=KeyboardInput(wVk=keyCode, dwFlags=EventF_KEYUP))
    SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

import ctypes
from ctypes import wintypes,windll
from JEAutoControl.Core.Util.Win32VK import *

user32 = ctypes.WinDLL('user32', use_last_error=True)

wintypes.ULONG_PTR = wintypes.WPARAM

Mouse = 0
Keyboard = 1
Hardware = 2

class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx", wintypes.LONG),
                ("dy", wintypes.LONG),
                ("mouseData", wintypes.DWORD),
                ("dwFlags", wintypes.DWORD),
                ("time", wintypes.DWORD),
                ("dwExtraInfo", ctypes.c_void_p))


class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk", wintypes.WORD),
                ("wScan", wintypes.WORD),
                ("dwFlags", wintypes.DWORD),
                ("time", wintypes.DWORD),
                ("dwExtraInfo", ctypes.c_void_p))

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        if not self.dwFlags & EventF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk,VkToVSC, 0)


class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg", wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))


class INPUT(ctypes.Structure):
    class INPUT_Union(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))

    _anonymous_ = ("_input",)
    _fields_ = (("type", wintypes.DWORD),
                ("_input", INPUT_Union))

LPINPUT = ctypes.POINTER(INPUT)


def _check_count(result,func,args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args

SendInput = user32.SendInput

user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (wintypes.UINT, ctypes.c_void_p, ctypes.c_int)
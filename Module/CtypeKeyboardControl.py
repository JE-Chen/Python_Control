import ctypes
from ctypes import wintypes

user32 = ctypes.WinDLL('user32', use_last_error=True)

Mouse = 0
Keyboard = 1
Hardware = 2

EventF_EXTENDEDKEY = 0x0001
EventF_KEYUP = 0x0002
EventF_UNICODE = 0x0004
EventF_SCANCODE = 0x0008

VkToVSC = 0

VK_BACK = 0x08
VK_TAB = 0x09
VK_CLEAR = 0x0C
VK_RETURN = 0x0D
VK_SHIFT = 0x10
VK_CONTROL = 0x11
VK_Menu = 0x12
VK_PAUSE = 0x13

wintypes.ULONG_PTR = wintypes.WPARAM


class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx", wintypes.LONG),
                ("dy", wintypes.LONG),
                ("mouseData", wintypes.DWORD),
                ("dwFlags", wintypes.DWORD),
                ("time", wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))


class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk", wintypes.WORD),
                ("wScan", wintypes.WORD),
                ("dwFlags", wintypes.DWORD),
                ("time", wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        # some programs use the scan code even if KEYEVENTF_SCANCODE
        # isn't set in dwFflags, so attempt to map the correct code.
        if not self.dwFlags & EventF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk,
                                                 VkToVSC, 0)


class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg", wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))


class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))

    _anonymous_ = ("_input",)
    _fields_ = (("type", wintypes.DWORD),
                ("_input", _INPUT))


LPINPUT = ctypes.POINTER(INPUT)


class CtypeKeyboardControl():

    def _check_count(self, result, args):
        if result == 0:
            raise ctypes.WinError(ctypes.get_last_error())
        return args

    user32.SendInput.errcheck = _check_count
    user32.SendInput.argtypes = (wintypes.UINT,  # nInputs
                                 LPINPUT,  # pInputs
                                 ctypes.c_int)  # cbSize

    # Functions

    def PressKey(self, hexKeyCode):
        x = INPUT(type=Keyboard,
                  ki=KEYBDINPUT(wVk=hexKeyCode))
        user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

    def ReleaseKey(self, hexKeyCode):
        x = INPUT(type=Keyboard,
                  ki=KEYBDINPUT(wVk=hexKeyCode,
                                dwFlags=EventF_KEYUP))
        user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


def PressTest():
    pass


if __name__ == "__main__":
    PressTest()

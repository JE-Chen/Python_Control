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

VK_BACK = 0x08 #BACKSPACE key
VK_TAB = 0x09 #TAB key
VK_CLEAR = 0x0C #CLEAR key
VK_RETURN = 0x0D #ENTER key
VK_SHIFT = 0x10 #SHIFT key
VK_CONTROL = 0x11 #CTRL key
VK_Menu = 0x12 #ALT key
VK_PAUSE = 0x13 #PAUSE key
VK_CAPITAL = 0x14 #CAPS LOCK key
VK_KANA = 0x15
VK_IME_ON = 0x16
VK_JUNJA = 0x17
VK_FINAL = 0x18 #ESC key
VK_HANJA = 0x19
VK_IME_OFF = 0x1A
VK_ESCAPE = 0x1B
VK_CONVERT = 0x1C
VK_NONCONVERT = 0x1D
VK_ACCEPT = 0x1E
VK_MODECHANGE = 0x1F
VK_SPACE = 0x20 #SPACEBAR
VK_PRIOR = 0x21 #PAGE UP key
VK_NEXT = 0x22 #PAGE DOWN key
VK_END = 0x23 #END key
VK_HOME = 0x24 #HOME key
VK_LEFT = 0x25 #LEFT ARROW key
VK_UP = 0x26
VK_RIGHT = 0x27
VK_DOWN = 0x28
VK_SELECT = 0x29
VK_PRINT = 0x2A
VK_EXECUTE = 0x2B
VK_SNAPSHOT = 0x2C
VK_INSERT = 0x2D
VK_DELETE = 0x2E
VK_HELP = 0x2F
key0 = 0x30
key1 = 0x31
key2 = 0x32
key3 = 0x33
key4 = 0x34
key5 = 0x35
key6 = 0x36
key7 = 0x37
key8 = 0x38
key9 = 0x39
keyA = 0x41
keyB = 0x42


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

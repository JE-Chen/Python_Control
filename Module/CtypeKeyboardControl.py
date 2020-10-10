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
keyC = 0x43
keyD = 0x44
keyE = 0x45
keyF = 0x46
keyG = 0x47
keyH = 0x48
keyI = 0x49
keyJ = 0x4A
keyK = 0x4B
keyL = 0x4C
keyM = 0X4D
keyN = 0x4E
keyO = 0x4F
keyP = 0x50
keyQ = 0x51
keyR = 0x52
keyS = 0x53
keyT = 0x54
keyU = 0x55
keyV = 0x56
keyW = 0x57
keyX = 0x58
keyY = 0x59
keyZ = 0x5A
VK_LWIN = 0x5B #Left Windows key (Natural keyboard)
VK_RWIN = 0x5C #Right Windows key (Natural keyboard)
VK_APPS = 0x5D #Applications key (Natural keyboard)
VK_SLEEP = 0x5F #Computer Sleep key
VK_NUMPAD0 = 0x60 #Numeric keypad 0 key
VK_NUMPAD1 = 0x61
VK_NUMPAD2 = 0x62
VK_NUMPAD3 = 0x63
VK_NUMPAD4 = 0x64
VK_NUMPAD5 = 0x65
VK_NUMPAD6 = 0x66
VK_NUMPAD7 = 0x67
VK_NUMPAD8 = 0x68
VK_NUMPAD9 = 0x69
VK_MULTIPLY = 0x6A #Multiply key
VK_ADD = 0x6B #Add key
VK_SEPARATOR = 0x6C # Separator key
VK_SUBTRACT = 0x6D # Subtract key
VK_DECIMAL = 0x6E # Decimal key
VK_DIVIDE = 0x6F # VK_DIVIDE
VK_F1 = 0x70 #F1
VK_F2 = 0x71
VK_F3 = 0x72
VK_F4 = 0x73
VK_F5 = 0x74
VK_F6 = 0x75
VK_F7 = 0x76
VK_F8 = 0x77
VK_F9 = 0x78
VK_F10 = 0x79
VK_F11 = 0x7A
VK_F12 = 0x7B
VK_F13 = 0x7C
VK_F14 = 0x7D
VK_F15 = 0x7E
VK_F16 = 0x7F
VK_F17 = 0x80
VK_F18 = 0x81
VK_F19 = 0x82
VK_F20 = 0x83
VK_F21 = 0x84
VK_F22 = 0x85
VK_F23 = 0x86
VK_F24 = 0x87
VK_NUMLOCK = 0x90 #NUM LOCK key
VK_SCROLL = 0x91 #SCROLL LOCK key
VK_LSHIFT = 0xA0 #Left SHIFT key
VK_RSHIFT = 0xA1
VK_LCONTROL = 0xA2 #Left CONTROL key
VK_RCONTROL = 0xA3 #Right CONTROL key
VK_LMENU = 0xA4 #Left MENU key
VK_RMENU = 0xA5 # Right MENU key
VK_BROWSER_BACK = 0xA6 #Browser Back key
VK_BROWSER_FORWARD = 0xA7 #Browser Forward key
VK_BROWSER_REFRESH = 0xA8 #Browser Refresh key
VK_BROWSER_STOP = 0xA9 #Browser Stop key
VK_BROWSER_SEARCH = 0xAA #Browser Search key
VK_BROWSER_FAVORITES = 0xAB #Browser Favorites key
VK_VOLUME_MUTE = 0xAD
VK_VOLUME_DOWN = 0xAE
VK_VOLUME_UP = 0xAF
VK_MEDIA_NEXT_TRACK = 0xB0
VK_MEDIA_PREV_TRACK = 0xB1
VK_MEDIA_STOP = 0xB2
VK_MEDIA_PLAY_PAUSE = 0xB3
VK_LAUNCH_MAIL = 0xB4
VK_LAUNCH_MEDIA_SELECT = 0xB5
VK_LAUNCH_APP1 = 0xB6
VK_LAUNCH_APP2 = 0xB7

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

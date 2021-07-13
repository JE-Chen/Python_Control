import sys

if sys.platform == "win32":
    from je_auto_control.windows.core.util.win32_vk import ABSOLUTE
    from je_auto_control.windows.core.util.win32_vk import EventF_EXTENDEDKEY
    from je_auto_control.windows.core.util.win32_vk import EventF_KEYUP
    from je_auto_control.windows.core.util.win32_vk import EventF_SCANCODE
    from je_auto_control.windows.core.util.win32_vk import EventF_UNICODE
    from je_auto_control.windows.core.util.win32_vk import HWHEEL
    from je_auto_control.windows.core.util.win32_vk import LEFTDOWN
    from je_auto_control.windows.core.util.win32_vk import LEFTUP
    from je_auto_control.windows.core.util.win32_vk import MIDDLEDOWN
    from je_auto_control.windows.core.util.win32_vk import MIDDLEUP
    from je_auto_control.windows.core.util.win32_vk import MOVE
    from je_auto_control.windows.core.util.win32_vk import RIGHTDOWN
    from je_auto_control.windows.core.util.win32_vk import RIGHTUP
    from je_auto_control.windows.core.util.win32_vk import VK_ACCEPT
    from je_auto_control.windows.core.util.win32_vk import VK_ADD
    from je_auto_control.windows.core.util.win32_vk import VK_APPS
    from je_auto_control.windows.core.util.win32_vk import VK_BACK
    from je_auto_control.windows.core.util.win32_vk import VK_BROWSER_BACK
    from je_auto_control.windows.core.util.win32_vk import VK_BROWSER_FAVORITES
    from je_auto_control.windows.core.util.win32_vk import VK_BROWSER_FORWARD
    from je_auto_control.windows.core.util.win32_vk import VK_BROWSER_REFRESH
    from je_auto_control.windows.core.util.win32_vk import VK_BROWSER_SEARCH
    from je_auto_control.windows.core.util.win32_vk import VK_BROWSER_STOP
    from je_auto_control.windows.core.util.win32_vk import VK_CANCEL
    from je_auto_control.windows.core.util.win32_vk import VK_CAPITAL
    from je_auto_control.windows.core.util.win32_vk import VK_CLEAR
    from je_auto_control.windows.core.util.win32_vk import VK_CONTROL
    from je_auto_control.windows.core.util.win32_vk import VK_CONVERT
    from je_auto_control.windows.core.util.win32_vk import VK_DECIMAL
    from je_auto_control.windows.core.util.win32_vk import VK_DELETE
    from je_auto_control.windows.core.util.win32_vk import VK_DIVIDE
    from je_auto_control.windows.core.util.win32_vk import VK_DOWN
    from je_auto_control.windows.core.util.win32_vk import VK_END
    from je_auto_control.windows.core.util.win32_vk import VK_ESCAPE
    from je_auto_control.windows.core.util.win32_vk import VK_EXECUTE
    from je_auto_control.windows.core.util.win32_vk import VK_F1
    from je_auto_control.windows.core.util.win32_vk import VK_F10
    from je_auto_control.windows.core.util.win32_vk import VK_F11
    from je_auto_control.windows.core.util.win32_vk import VK_F12
    from je_auto_control.windows.core.util.win32_vk import VK_F13
    from je_auto_control.windows.core.util.win32_vk import VK_F14
    from je_auto_control.windows.core.util.win32_vk import VK_F15
    from je_auto_control.windows.core.util.win32_vk import VK_F16
    from je_auto_control.windows.core.util.win32_vk import VK_F17
    from je_auto_control.windows.core.util.win32_vk import VK_F18
    from je_auto_control.windows.core.util.win32_vk import VK_F19
    from je_auto_control.windows.core.util.win32_vk import VK_F2
    from je_auto_control.windows.core.util.win32_vk import VK_F20
    from je_auto_control.windows.core.util.win32_vk import VK_F21
    from je_auto_control.windows.core.util.win32_vk import VK_F22
    from je_auto_control.windows.core.util.win32_vk import VK_F23
    from je_auto_control.windows.core.util.win32_vk import VK_F24
    from je_auto_control.windows.core.util.win32_vk import VK_F3
    from je_auto_control.windows.core.util.win32_vk import VK_F4
    from je_auto_control.windows.core.util.win32_vk import VK_F5
    from je_auto_control.windows.core.util.win32_vk import VK_F6
    from je_auto_control.windows.core.util.win32_vk import VK_F7
    from je_auto_control.windows.core.util.win32_vk import VK_F8
    from je_auto_control.windows.core.util.win32_vk import VK_F9
    from je_auto_control.windows.core.util.win32_vk import VK_FINAL
    from je_auto_control.windows.core.util.win32_vk import VK_HANJA
    from je_auto_control.windows.core.util.win32_vk import VK_HELP
    from je_auto_control.windows.core.util.win32_vk import VK_HOME
    from je_auto_control.windows.core.util.win32_vk import VK_IME_OFF
    from je_auto_control.windows.core.util.win32_vk import VK_IME_ON
    from je_auto_control.windows.core.util.win32_vk import VK_INSERT
    from je_auto_control.windows.core.util.win32_vk import VK_JUNJA
    from je_auto_control.windows.core.util.win32_vk import VK_KANA
    from je_auto_control.windows.core.util.win32_vk import VK_LAUNCH_APP1
    from je_auto_control.windows.core.util.win32_vk import VK_LAUNCH_APP2
    from je_auto_control.windows.core.util.win32_vk import VK_LAUNCH_MAIL
    from je_auto_control.windows.core.util.win32_vk import VK_LAUNCH_MEDIA_SELECT
    from je_auto_control.windows.core.util.win32_vk import VK_LBUTTON
    from je_auto_control.windows.core.util.win32_vk import VK_LCONTROL
    from je_auto_control.windows.core.util.win32_vk import VK_LEFT
    from je_auto_control.windows.core.util.win32_vk import VK_LMENU
    from je_auto_control.windows.core.util.win32_vk import VK_LSHIFT
    from je_auto_control.windows.core.util.win32_vk import VK_LWIN
    from je_auto_control.windows.core.util.win32_vk import VK_MBUTTON
    from je_auto_control.windows.core.util.win32_vk import VK_MEDIA_NEXT_TRACK
    from je_auto_control.windows.core.util.win32_vk import VK_MEDIA_PLAY_PAUSE
    from je_auto_control.windows.core.util.win32_vk import VK_MEDIA_PREV_TRACK
    from je_auto_control.windows.core.util.win32_vk import VK_MEDIA_STOP
    from je_auto_control.windows.core.util.win32_vk import VK_MODECHANGE
    from je_auto_control.windows.core.util.win32_vk import VK_MULTIPLY
    from je_auto_control.windows.core.util.win32_vk import VK_Menu
    from je_auto_control.windows.core.util.win32_vk import VK_NEXT
    from je_auto_control.windows.core.util.win32_vk import VK_NONCONVERT
    from je_auto_control.windows.core.util.win32_vk import VK_NUMLOCK
    from je_auto_control.windows.core.util.win32_vk import VK_NUMPAD0
    from je_auto_control.windows.core.util.win32_vk import VK_NUMPAD1
    from je_auto_control.windows.core.util.win32_vk import VK_NUMPAD2
    from je_auto_control.windows.core.util.win32_vk import VK_NUMPAD3
    from je_auto_control.windows.core.util.win32_vk import VK_NUMPAD4
    from je_auto_control.windows.core.util.win32_vk import VK_NUMPAD5
    from je_auto_control.windows.core.util.win32_vk import VK_NUMPAD6
    from je_auto_control.windows.core.util.win32_vk import VK_NUMPAD7
    from je_auto_control.windows.core.util.win32_vk import VK_NUMPAD8
    from je_auto_control.windows.core.util.win32_vk import VK_NUMPAD9
    from je_auto_control.windows.core.util.win32_vk import VK_PAUSE
    from je_auto_control.windows.core.util.win32_vk import VK_PRINT
    from je_auto_control.windows.core.util.win32_vk import VK_PRIOR
    from je_auto_control.windows.core.util.win32_vk import VK_RBUTTON
    from je_auto_control.windows.core.util.win32_vk import VK_RCONTROL
    from je_auto_control.windows.core.util.win32_vk import VK_RETURN
    from je_auto_control.windows.core.util.win32_vk import VK_RIGHT
    from je_auto_control.windows.core.util.win32_vk import VK_RMENU
    from je_auto_control.windows.core.util.win32_vk import VK_RSHIFT
    from je_auto_control.windows.core.util.win32_vk import VK_RWIN
    from je_auto_control.windows.core.util.win32_vk import VK_SCROLL
    from je_auto_control.windows.core.util.win32_vk import VK_SELECT
    from je_auto_control.windows.core.util.win32_vk import VK_SEPARATOR
    from je_auto_control.windows.core.util.win32_vk import VK_SHIFT
    from je_auto_control.windows.core.util.win32_vk import VK_SLEEP
    from je_auto_control.windows.core.util.win32_vk import VK_SNAPSHOT
    from je_auto_control.windows.core.util.win32_vk import VK_SPACE
    from je_auto_control.windows.core.util.win32_vk import VK_SUBTRACT
    from je_auto_control.windows.core.util.win32_vk import VK_TAB
    from je_auto_control.windows.core.util.win32_vk import VK_UP
    from je_auto_control.windows.core.util.win32_vk import VK_VOLUME_DOWN
    from je_auto_control.windows.core.util.win32_vk import VK_VOLUME_MUTE
    from je_auto_control.windows.core.util.win32_vk import VK_VOLUME_UP
    from je_auto_control.windows.core.util.win32_vk import VK_XBUTTON1
    from je_auto_control.windows.core.util.win32_vk import VK_XBUTTON2
    from je_auto_control.windows.core.util.win32_vk import VkToVSC
    from je_auto_control.windows.core.util.win32_vk import WHEEL
    from je_auto_control.windows.core.util.win32_vk import XBUTTON1
    from je_auto_control.windows.core.util.win32_vk import XBUTTON2
    from je_auto_control.windows.core.util.win32_vk import XDOWN
    from je_auto_control.windows.core.util.win32_vk import XUP
    from je_auto_control.windows.core.util.win32_vk import key0
    from je_auto_control.windows.core.util.win32_vk import key1
    from je_auto_control.windows.core.util.win32_vk import key2
    from je_auto_control.windows.core.util.win32_vk import key3
    from je_auto_control.windows.core.util.win32_vk import key4
    from je_auto_control.windows.core.util.win32_vk import key5
    from je_auto_control.windows.core.util.win32_vk import key6
    from je_auto_control.windows.core.util.win32_vk import key7
    from je_auto_control.windows.core.util.win32_vk import key8
    from je_auto_control.windows.core.util.win32_vk import key9
    from je_auto_control.windows.core.util.win32_vk import keyA
    from je_auto_control.windows.core.util.win32_vk import keyB
    from je_auto_control.windows.core.util.win32_vk import keyC
    from je_auto_control.windows.core.util.win32_vk import keyD
    from je_auto_control.windows.core.util.win32_vk import keyE
    from je_auto_control.windows.core.util.win32_vk import keyF
    from je_auto_control.windows.core.util.win32_vk import keyG
    from je_auto_control.windows.core.util.win32_vk import keyH
    from je_auto_control.windows.core.util.win32_vk import keyI
    from je_auto_control.windows.core.util.win32_vk import keyJ
    from je_auto_control.windows.core.util.win32_vk import keyK
    from je_auto_control.windows.core.util.win32_vk import keyL
    from je_auto_control.windows.core.util.win32_vk import keyM
    from je_auto_control.windows.core.util.win32_vk import keyN
    from je_auto_control.windows.core.util.win32_vk import keyO
    from je_auto_control.windows.core.util.win32_vk import keyP
    from je_auto_control.windows.core.util.win32_vk import keyQ
    from je_auto_control.windows.core.util.win32_vk import keyR
    from je_auto_control.windows.core.util.win32_vk import keyS
    from je_auto_control.windows.core.util.win32_vk import keyT
    from je_auto_control.windows.core.util.win32_vk import keyU
    from je_auto_control.windows.core.util.win32_vk import keyV
    from je_auto_control.windows.core.util.win32_vk import keyW
    from je_auto_control.windows.core.util.win32_vk import keyX
    from je_auto_control.windows.core.util.win32_vk import keyY
    from je_auto_control.windows.core.util.win32_vk import keyZ
    from je_auto_control.windows.keyboard import win32_ctype_keyboard_control
    from je_auto_control.windows.mouse import win32_ctype_mouse_control
    from je_auto_control.windows.screen import screen

elif sys.platform == "darwin":
    pass

elif sys.platform not in ("darwin", "win32"):
    pass

else:
    raise Exception("unknown operating system")

from je_auto_control.util import template_detection

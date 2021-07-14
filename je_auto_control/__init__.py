import sys

if sys.platform in ["win32", "cygwin", "msys"]:
    from je_auto_control.windows.core.util.win32_vk import win32_ABSOLUTE
    from je_auto_control.windows.core.util.win32_vk import win32_EventF_EXTENDEDKEY
    from je_auto_control.windows.core.util.win32_vk import win32_EventF_KEYUP
    from je_auto_control.windows.core.util.win32_vk import win32_EventF_SCANCODE
    from je_auto_control.windows.core.util.win32_vk import win32_EventF_UNICODE
    from je_auto_control.windows.core.util.win32_vk import win32_HWHEEL
    from je_auto_control.windows.core.util.win32_vk import win32_LEFTDOWN
    from je_auto_control.windows.core.util.win32_vk import win32_LEFTUP
    from je_auto_control.windows.core.util.win32_vk import win32_MIDDLEDOWN
    from je_auto_control.windows.core.util.win32_vk import win32_MIDDLEUP
    from je_auto_control.windows.core.util.win32_vk import win32_MOVE
    from je_auto_control.windows.core.util.win32_vk import win32_RIGHTDOWN
    from je_auto_control.windows.core.util.win32_vk import win32_RIGHTUP
    from je_auto_control.windows.core.util.win32_vk import win32_VK_ACCEPT
    from je_auto_control.windows.core.util.win32_vk import win32_VK_ADD
    from je_auto_control.windows.core.util.win32_vk import win32_VK_APPS
    from je_auto_control.windows.core.util.win32_vk import win32_VK_BACK
    from je_auto_control.windows.core.util.win32_vk import win32_VK_BROWSER_BACK
    from je_auto_control.windows.core.util.win32_vk import win32_VK_BROWSER_FAVORITES
    from je_auto_control.windows.core.util.win32_vk import win32_VK_BROWSER_FORWARD
    from je_auto_control.windows.core.util.win32_vk import win32_VK_BROWSER_REFRESH
    from je_auto_control.windows.core.util.win32_vk import win32_VK_BROWSER_SEARCH
    from je_auto_control.windows.core.util.win32_vk import win32_VK_BROWSER_STOP
    from je_auto_control.windows.core.util.win32_vk import win32_VK_CANCEL
    from je_auto_control.windows.core.util.win32_vk import win32_VK_CAPITAL
    from je_auto_control.windows.core.util.win32_vk import win32_VK_CLEAR
    from je_auto_control.windows.core.util.win32_vk import win32_VK_CONTROL
    from je_auto_control.windows.core.util.win32_vk import win32_VK_CONVERT
    from je_auto_control.windows.core.util.win32_vk import win32_VK_DECIMAL
    from je_auto_control.windows.core.util.win32_vk import win32_VK_DELETE
    from je_auto_control.windows.core.util.win32_vk import win32_VK_DIVIDE
    from je_auto_control.windows.core.util.win32_vk import win32_VK_DOWN
    from je_auto_control.windows.core.util.win32_vk import win32_VK_END
    from je_auto_control.windows.core.util.win32_vk import win32_VK_ESCAPE
    from je_auto_control.windows.core.util.win32_vk import win32_VK_EXECUTE
    from je_auto_control.windows.core.util.win32_vk import win32_VK_F1
    from je_auto_control.windows.core.util.win32_vk import win32_VK_F10
    from je_auto_control.windows.core.util.win32_vk import win32_VK_F11
    from je_auto_control.windows.core.util.win32_vk import win32_VK_F12
    from je_auto_control.windows.core.util.win32_vk import win32_VK_F13
    from je_auto_control.windows.core.util.win32_vk import win32_VK_F14
    from je_auto_control.windows.core.util.win32_vk import win32_VK_F15
    from je_auto_control.windows.core.util.win32_vk import win32_VK_F16
    from je_auto_control.windows.core.util.win32_vk import win32_VK_F17
    from je_auto_control.windows.core.util.win32_vk import win32_VK_F18
    from je_auto_control.windows.core.util.win32_vk import win32_VK_F19
    from je_auto_control.windows.core.util.win32_vk import win32_VK_F2
    from je_auto_control.windows.core.util.win32_vk import win32_VK_F20
    from je_auto_control.windows.core.util.win32_vk import win32_VK_F21
    from je_auto_control.windows.core.util.win32_vk import win32_VK_F22
    from je_auto_control.windows.core.util.win32_vk import win32_VK_F23
    from je_auto_control.windows.core.util.win32_vk import win32_VK_F24
    from je_auto_control.windows.core.util.win32_vk import win32_VK_F3
    from je_auto_control.windows.core.util.win32_vk import win32_VK_F4
    from je_auto_control.windows.core.util.win32_vk import win32_VK_F5
    from je_auto_control.windows.core.util.win32_vk import win32_VK_F6
    from je_auto_control.windows.core.util.win32_vk import win32_VK_F7
    from je_auto_control.windows.core.util.win32_vk import win32_VK_F8
    from je_auto_control.windows.core.util.win32_vk import win32_VK_F9
    from je_auto_control.windows.core.util.win32_vk import win32_VK_FINAL
    from je_auto_control.windows.core.util.win32_vk import win32_VK_HANJA
    from je_auto_control.windows.core.util.win32_vk import win32_VK_HELP
    from je_auto_control.windows.core.util.win32_vk import win32_VK_HOME
    from je_auto_control.windows.core.util.win32_vk import win32_VK_IME_OFF
    from je_auto_control.windows.core.util.win32_vk import win32_VK_IME_ON
    from je_auto_control.windows.core.util.win32_vk import win32_VK_INSERT
    from je_auto_control.windows.core.util.win32_vk import win32_VK_JUNJA
    from je_auto_control.windows.core.util.win32_vk import win32_VK_KANA
    from je_auto_control.windows.core.util.win32_vk import win32_VK_LAUNCH_APP1
    from je_auto_control.windows.core.util.win32_vk import win32_VK_LAUNCH_APP2
    from je_auto_control.windows.core.util.win32_vk import win32_VK_LAUNCH_MAIL
    from je_auto_control.windows.core.util.win32_vk import win32_VK_LAUNCH_MEDIA_SELECT
    from je_auto_control.windows.core.util.win32_vk import win32_VK_LBUTTON
    from je_auto_control.windows.core.util.win32_vk import win32_VK_LCONTROL
    from je_auto_control.windows.core.util.win32_vk import win32_VK_LEFT
    from je_auto_control.windows.core.util.win32_vk import win32_VK_LMENU
    from je_auto_control.windows.core.util.win32_vk import win32_VK_LSHIFT
    from je_auto_control.windows.core.util.win32_vk import win32_VK_LWIN
    from je_auto_control.windows.core.util.win32_vk import win32_VK_MBUTTON
    from je_auto_control.windows.core.util.win32_vk import win32_VK_MEDIA_NEXT_TRACK
    from je_auto_control.windows.core.util.win32_vk import win32_VK_MEDIA_PLAY_PAUSE
    from je_auto_control.windows.core.util.win32_vk import win32_VK_MEDIA_PREV_TRACK
    from je_auto_control.windows.core.util.win32_vk import win32_VK_MEDIA_STOP
    from je_auto_control.windows.core.util.win32_vk import win32_VK_MODECHANGE
    from je_auto_control.windows.core.util.win32_vk import win32_VK_MULTIPLY
    from je_auto_control.windows.core.util.win32_vk import win32_VK_Menu
    from je_auto_control.windows.core.util.win32_vk import win32_VK_NEXT
    from je_auto_control.windows.core.util.win32_vk import win32_VK_NONCONVERT
    from je_auto_control.windows.core.util.win32_vk import win32_VK_NUMLOCK
    from je_auto_control.windows.core.util.win32_vk import win32_VK_NUMPAD0
    from je_auto_control.windows.core.util.win32_vk import win32_VK_NUMPAD1
    from je_auto_control.windows.core.util.win32_vk import win32_VK_NUMPAD2
    from je_auto_control.windows.core.util.win32_vk import win32_VK_NUMPAD3
    from je_auto_control.windows.core.util.win32_vk import win32_VK_NUMPAD4
    from je_auto_control.windows.core.util.win32_vk import win32_VK_NUMPAD5
    from je_auto_control.windows.core.util.win32_vk import win32_VK_NUMPAD6
    from je_auto_control.windows.core.util.win32_vk import win32_VK_NUMPAD7
    from je_auto_control.windows.core.util.win32_vk import win32_VK_NUMPAD8
    from je_auto_control.windows.core.util.win32_vk import win32_VK_NUMPAD9
    from je_auto_control.windows.core.util.win32_vk import win32_VK_PAUSE
    from je_auto_control.windows.core.util.win32_vk import win32_VK_PRINT
    from je_auto_control.windows.core.util.win32_vk import win32_VK_PRIOR
    from je_auto_control.windows.core.util.win32_vk import win32_VK_RBUTTON
    from je_auto_control.windows.core.util.win32_vk import win32_VK_RCONTROL
    from je_auto_control.windows.core.util.win32_vk import win32_VK_RETURN
    from je_auto_control.windows.core.util.win32_vk import win32_VK_RIGHT
    from je_auto_control.windows.core.util.win32_vk import win32_VK_RMENU
    from je_auto_control.windows.core.util.win32_vk import win32_VK_RSHIFT
    from je_auto_control.windows.core.util.win32_vk import win32_VK_RWIN
    from je_auto_control.windows.core.util.win32_vk import win32_VK_SCROLL
    from je_auto_control.windows.core.util.win32_vk import win32_VK_SELECT
    from je_auto_control.windows.core.util.win32_vk import win32_VK_SEPARATOR
    from je_auto_control.windows.core.util.win32_vk import win32_VK_SHIFT
    from je_auto_control.windows.core.util.win32_vk import win32_VK_SLEEP
    from je_auto_control.windows.core.util.win32_vk import win32_VK_SNAPSHOT
    from je_auto_control.windows.core.util.win32_vk import win32_VK_SPACE
    from je_auto_control.windows.core.util.win32_vk import win32_VK_SUBTRACT
    from je_auto_control.windows.core.util.win32_vk import win32_VK_TAB
    from je_auto_control.windows.core.util.win32_vk import win32_VK_UP
    from je_auto_control.windows.core.util.win32_vk import win32_VK_VOLUME_DOWN
    from je_auto_control.windows.core.util.win32_vk import win32_VK_VOLUME_MUTE
    from je_auto_control.windows.core.util.win32_vk import win32_VK_VOLUME_UP
    from je_auto_control.windows.core.util.win32_vk import win32_VK_XBUTTON1
    from je_auto_control.windows.core.util.win32_vk import win32_VK_XBUTTON2
    from je_auto_control.windows.core.util.win32_vk import win32_VkToVSC
    from je_auto_control.windows.core.util.win32_vk import win32_WHEEL
    from je_auto_control.windows.core.util.win32_vk import win32_XBUTTON1
    from je_auto_control.windows.core.util.win32_vk import win32_XBUTTON2
    from je_auto_control.windows.core.util.win32_vk import win32_DOWN
    from je_auto_control.windows.core.util.win32_vk import win32_XUP
    from je_auto_control.windows.core.util.win32_vk import win32_key0
    from je_auto_control.windows.core.util.win32_vk import win32_key1
    from je_auto_control.windows.core.util.win32_vk import win32_key2
    from je_auto_control.windows.core.util.win32_vk import win32_key3
    from je_auto_control.windows.core.util.win32_vk import win32_key4
    from je_auto_control.windows.core.util.win32_vk import win32_key5
    from je_auto_control.windows.core.util.win32_vk import win32_key6
    from je_auto_control.windows.core.util.win32_vk import win32_key7
    from je_auto_control.windows.core.util.win32_vk import win32_key8
    from je_auto_control.windows.core.util.win32_vk import win32_key9
    from je_auto_control.windows.core.util.win32_vk import win32_keyA
    from je_auto_control.windows.core.util.win32_vk import win32_keyB
    from je_auto_control.windows.core.util.win32_vk import win32_keyC
    from je_auto_control.windows.core.util.win32_vk import win32_keyD
    from je_auto_control.windows.core.util.win32_vk import win32_keyE
    from je_auto_control.windows.core.util.win32_vk import win32_keyF
    from je_auto_control.windows.core.util.win32_vk import win32_keyG
    from je_auto_control.windows.core.util.win32_vk import win32_keyH
    from je_auto_control.windows.core.util.win32_vk import win32_keyI
    from je_auto_control.windows.core.util.win32_vk import win32_keyJ
    from je_auto_control.windows.core.util.win32_vk import win32_keyK
    from je_auto_control.windows.core.util.win32_vk import win32_keyL
    from je_auto_control.windows.core.util.win32_vk import win32_keyM
    from je_auto_control.windows.core.util.win32_vk import win32_keyN
    from je_auto_control.windows.core.util.win32_vk import win32_keyO
    from je_auto_control.windows.core.util.win32_vk import win32_keyP
    from je_auto_control.windows.core.util.win32_vk import win32_keyQ
    from je_auto_control.windows.core.util.win32_vk import win32_keyR
    from je_auto_control.windows.core.util.win32_vk import win32_keyS
    from je_auto_control.windows.core.util.win32_vk import win32_keyT
    from je_auto_control.windows.core.util.win32_vk import win32_keyU
    from je_auto_control.windows.core.util.win32_vk import win32_keyV
    from je_auto_control.windows.core.util.win32_vk import win32_keyW
    from je_auto_control.windows.core.util.win32_vk import win32_keyX
    from je_auto_control.windows.core.util.win32_vk import win32_keyY
    from je_auto_control.windows.core.util.win32_vk import win32_keyZ
    from je_auto_control.windows.keyboard import win32_ctype_keyboard_control
    from je_auto_control.windows.mouse import win32_ctype_mouse_control
    from je_auto_control.windows.screen import win32_screen

elif sys.platform in ["darwin"]:
    pass

elif sys.platform in ["linux", "linux2"]:
    pass

else:
    raise Exception("unknown operating system")

from je_auto_control.util import template_detection

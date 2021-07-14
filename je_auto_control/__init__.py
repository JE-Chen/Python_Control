import sys

if sys.platform in ["win32", "cygwin", "msys"]:
    from je_auto_control.windows.core.utils.win32_vk import win32_ABSOLUTE
    from je_auto_control.windows.core.utils.win32_vk import win32_EventF_EXTENDEDKEY
    from je_auto_control.windows.core.utils.win32_vk import win32_EventF_KEYUP
    from je_auto_control.windows.core.utils.win32_vk import win32_EventF_SCANCODE
    from je_auto_control.windows.core.utils.win32_vk import win32_EventF_UNICODE
    from je_auto_control.windows.core.utils.win32_vk import win32_HWHEEL
    from je_auto_control.windows.core.utils.win32_vk import win32_LEFTDOWN
    from je_auto_control.windows.core.utils.win32_vk import win32_LEFTUP
    from je_auto_control.windows.core.utils.win32_vk import win32_MIDDLEDOWN
    from je_auto_control.windows.core.utils.win32_vk import win32_MIDDLEUP
    from je_auto_control.windows.core.utils.win32_vk import win32_MOVE
    from je_auto_control.windows.core.utils.win32_vk import win32_RIGHTDOWN
    from je_auto_control.windows.core.utils.win32_vk import win32_RIGHTUP
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_ACCEPT
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_ADD
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_APPS
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_BACK
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_BROWSER_BACK
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_BROWSER_FAVORITES
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_BROWSER_FORWARD
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_BROWSER_REFRESH
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_BROWSER_SEARCH
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_BROWSER_STOP
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_CANCEL
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_CAPITAL
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_CLEAR
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_CONTROL
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_CONVERT
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_DECIMAL
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_DELETE
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_DIVIDE
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_DOWN
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_END
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_ESCAPE
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_EXECUTE
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_F1
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_F10
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_F11
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_F12
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_F13
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_F14
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_F15
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_F16
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_F17
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_F18
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_F19
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_F2
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_F20
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_F21
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_F22
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_F23
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_F24
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_F3
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_F4
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_F5
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_F6
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_F7
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_F8
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_F9
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_FINAL
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_HANJA
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_HELP
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_HOME
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_IME_OFF
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_IME_ON
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_INSERT
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_JUNJA
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_KANA
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_LAUNCH_APP1
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_LAUNCH_APP2
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_LAUNCH_MAIL
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_LAUNCH_MEDIA_SELECT
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_LBUTTON
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_LCONTROL
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_LEFT
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_LMENU
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_LSHIFT
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_LWIN
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_MBUTTON
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_MEDIA_NEXT_TRACK
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_MEDIA_PLAY_PAUSE
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_MEDIA_PREV_TRACK
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_MEDIA_STOP
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_MODECHANGE
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_MULTIPLY
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_Menu
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_NEXT
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_NONCONVERT
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_NUMLOCK
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_NUMPAD0
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_NUMPAD1
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_NUMPAD2
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_NUMPAD3
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_NUMPAD4
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_NUMPAD5
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_NUMPAD6
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_NUMPAD7
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_NUMPAD8
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_NUMPAD9
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_PAUSE
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_PRINT
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_PRIOR
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_RBUTTON
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_RCONTROL
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_RETURN
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_RIGHT
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_RMENU
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_RSHIFT
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_RWIN
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_SCROLL
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_SELECT
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_SEPARATOR
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_SHIFT
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_SLEEP
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_SNAPSHOT
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_SPACE
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_SUBTRACT
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_TAB
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_UP
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_VOLUME_DOWN
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_VOLUME_MUTE
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_VOLUME_UP
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_XBUTTON1
    from je_auto_control.windows.core.utils.win32_vk import win32_VK_XBUTTON2
    from je_auto_control.windows.core.utils.win32_vk import win32_VkToVSC
    from je_auto_control.windows.core.utils.win32_vk import win32_WHEEL
    from je_auto_control.windows.core.utils.win32_vk import win32_XBUTTON1
    from je_auto_control.windows.core.utils.win32_vk import win32_XBUTTON2
    from je_auto_control.windows.core.utils.win32_vk import win32_DOWN
    from je_auto_control.windows.core.utils.win32_vk import win32_XUP
    from je_auto_control.windows.core.utils.win32_vk import win32_key0
    from je_auto_control.windows.core.utils.win32_vk import win32_key1
    from je_auto_control.windows.core.utils.win32_vk import win32_key2
    from je_auto_control.windows.core.utils.win32_vk import win32_key3
    from je_auto_control.windows.core.utils.win32_vk import win32_key4
    from je_auto_control.windows.core.utils.win32_vk import win32_key5
    from je_auto_control.windows.core.utils.win32_vk import win32_key6
    from je_auto_control.windows.core.utils.win32_vk import win32_key7
    from je_auto_control.windows.core.utils.win32_vk import win32_key8
    from je_auto_control.windows.core.utils.win32_vk import win32_key9
    from je_auto_control.windows.core.utils.win32_vk import win32_keyA
    from je_auto_control.windows.core.utils.win32_vk import win32_keyB
    from je_auto_control.windows.core.utils.win32_vk import win32_keyC
    from je_auto_control.windows.core.utils.win32_vk import win32_keyD
    from je_auto_control.windows.core.utils.win32_vk import win32_keyE
    from je_auto_control.windows.core.utils.win32_vk import win32_keyF
    from je_auto_control.windows.core.utils.win32_vk import win32_keyG
    from je_auto_control.windows.core.utils.win32_vk import win32_keyH
    from je_auto_control.windows.core.utils.win32_vk import win32_keyI
    from je_auto_control.windows.core.utils.win32_vk import win32_keyJ
    from je_auto_control.windows.core.utils.win32_vk import win32_keyK
    from je_auto_control.windows.core.utils.win32_vk import win32_keyL
    from je_auto_control.windows.core.utils.win32_vk import win32_keyM
    from je_auto_control.windows.core.utils.win32_vk import win32_keyN
    from je_auto_control.windows.core.utils.win32_vk import win32_keyO
    from je_auto_control.windows.core.utils.win32_vk import win32_keyP
    from je_auto_control.windows.core.utils.win32_vk import win32_keyQ
    from je_auto_control.windows.core.utils.win32_vk import win32_keyR
    from je_auto_control.windows.core.utils.win32_vk import win32_keyS
    from je_auto_control.windows.core.utils.win32_vk import win32_keyT
    from je_auto_control.windows.core.utils.win32_vk import win32_keyU
    from je_auto_control.windows.core.utils.win32_vk import win32_keyV
    from je_auto_control.windows.core.utils.win32_vk import win32_keyW
    from je_auto_control.windows.core.utils.win32_vk import win32_keyX
    from je_auto_control.windows.core.utils.win32_vk import win32_keyY
    from je_auto_control.windows.core.utils.win32_vk import win32_keyZ
    from je_auto_control.windows.keyboard import win32_ctype_keyboard_control
    from je_auto_control.windows.mouse import win32_ctype_mouse_control
    from je_auto_control.windows.screen import win32_screen

elif sys.platform in ["darwin"]:
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_backspace
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_slash_b
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_tab
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_enter
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_return
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_shift
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_ctrl
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_alt
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_pause
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_capslock
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_esc
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_escape
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_pgup
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_pgdn
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_pageup
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_pagedown
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_end
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_home
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_left
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_up
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_right
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_down
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_select
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_print
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_execute
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_prtsc
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_prtscr
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_prntscrn
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_insert
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_del
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_delete
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_help
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_win
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_winleft
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_winright
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_apps
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_num0
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_num1
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_num2
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_num3
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_num4
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_num5
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_num6
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_num7
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_num8
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_num9
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_multiply
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_add
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_separator
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_subtract
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_decimal
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_divide
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_f1
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_f2
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_f3
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_f4
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_f5
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_f6
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_f7
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_f8
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_f9
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_f10
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_f11
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_f12
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_f13
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_f14
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_f15
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_f16
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_f17
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_f18
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_f19
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_f20
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_f21
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_f22
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_f23
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_f24
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_numlock
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_scrolllock
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_shiftleft
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_shiftright
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_ctrlleft
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_ctrlright
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_altleft
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_altright
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_space
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_newline_n
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_newline_r
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_newline_t
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_exclam
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_numbersign
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_percent
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_dollar
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_ampersand
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_quotedbl
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_apostrophe
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_parenleft
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_parenright
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_asterisk
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_equal
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_plus
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_comma
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_minus
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_period
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_slash
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_colon
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_semicolon
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_less
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_greater
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_question
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_at
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_bracketleft
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_bracketright
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_backslash
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_asciicircum
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_underscore
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_grave
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_braceleft
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_bar
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_braceright
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_asciitilde
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_a
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_b
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_c
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_d
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_e
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_f
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_g
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_h
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_i
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_j
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_k
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_l
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_m
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_n
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_o
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_p
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_q
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_r
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_s
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_t
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_u
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_v
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_w
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_x
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_y
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_z
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_A
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_B
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_C
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_D
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_E
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_F
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_G
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_H
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_I
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_J
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_K
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_L
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_M
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_N
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_O
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_P
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_Q
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_R
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_S
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_T
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_U
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_V
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_W
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_X
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_Y
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_Z
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_1
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_2
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_3
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_4
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_5
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_6
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_7
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_8
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_9
    from je_auto_control.linux_with_x11.core.utils.x11_linux_vk import x11_linux_key_0

elif sys.platform in ["linux", "linux2"]:
    pass

else:
    raise Exception("unknown operating system")

from je_auto_control.utils import template_detection

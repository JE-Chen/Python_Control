import sys

from je_auto_control import win32_keyT
from je_auto_control import win32_keyE
from je_auto_control import win32_keyS
from je_auto_control import win32_ctype_keyboard_control as keyboard_control

print(sys.platform)

keyboard_control.press_key(win32_keyT)
keyboard_control.press_key(win32_keyE)
keyboard_control.press_key(win32_keyS)
keyboard_control.press_key(win32_keyT)

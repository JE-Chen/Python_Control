import time
from je_auto_control import x11_linux_keyboard_control as linux_keyboard
from je_auto_control import x11_linux_key_t
from je_auto_control import x11_linux_key_e
from je_auto_control import x11_linux_key_s

linux_keyboard.press_key(x11_linux_key_t)
linux_keyboard.release_key(x11_linux_key_t)
time.sleep(.05)
linux_keyboard.press_key(x11_linux_key_e)
linux_keyboard.release_key(x11_linux_key_e)
time.sleep(.05)
linux_keyboard.press_key(x11_linux_key_s)
linux_keyboard.release_key(x11_linux_key_s)
time.sleep(.05)
linux_keyboard.press_key(x11_linux_key_t)
linux_keyboard.release_key(x11_linux_key_t)

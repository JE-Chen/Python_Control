from Xlib import X
from Xlib.ext.xtest import fake_input

from je_auto_control.linux_with_x11.core.display import display


def press_key(keycode):
    fake_input(display, X.KeyPress, keycode)
    display.sync()


def release_key(keycode):
    fake_input(display, X.KeyRelease, keycode)
    display.sync()

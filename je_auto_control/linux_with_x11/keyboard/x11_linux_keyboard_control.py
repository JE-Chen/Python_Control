from je_auto_control.linux_with_x11.core.x11_linux_display import display
from Xlib.ext.xtest import fake_input
from Xlib import X


def press_key(keycode):
    fake_input(display, X.KeyPress, keycode)
    display.sync()


def release_key(keycode):
    fake_input(display, X.KeyRelease, keycode)
    display.sync()

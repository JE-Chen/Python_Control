from Xlib import X
from Xlib.ext.xtest import fake_input

from je_auto_control.linux_with_x11.core.display import display


def position():
    coord = display.screen().root.query_pointer()._data
    return coord["root_x"], coord["root_y"]


def set_position(x, y):
    fake_input(display, X.MotionNotify, x=x, y=y)
    display.sync()

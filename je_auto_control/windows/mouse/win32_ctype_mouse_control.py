from je_auto_control.windows.core.util.win32_ctype_input import Input
from je_auto_control.windows.core.util.win32_ctype_input import LEFTDOWN
from je_auto_control.windows.core.util.win32_ctype_input import LEFTUP
from je_auto_control.windows.core.util.win32_ctype_input import MIDDLEDOWN
from je_auto_control.windows.core.util.win32_ctype_input import MIDDLEUP
from je_auto_control.windows.core.util.win32_ctype_input import Mouse
from je_auto_control.windows.core.util.win32_ctype_input import MouseInput
from je_auto_control.windows.core.util.win32_ctype_input import RIGHTDOWN
from je_auto_control.windows.core.util.win32_ctype_input import RIGHTUP
from je_auto_control.windows.core.util.win32_ctype_input import SendInput
from je_auto_control.windows.core.util.win32_ctype_input import XBUTTON1
from je_auto_control.windows.core.util.win32_ctype_input import XBUTTON2
from je_auto_control.windows.core.util.win32_ctype_input import XDOWN
from je_auto_control.windows.core.util.win32_ctype_input import XUP
from je_auto_control.windows.core.util.win32_ctype_input import ctypes
from je_auto_control.windows.core.util.win32_ctype_input import windll
from je_auto_control.windows.core.util.win32_ctype_input import wintypes
from je_auto_control.windows.core.util.win32_ctype_mouse_event import mouse_event
from je_auto_control.windows.core.util.win32_vk import WHEEL
from je_auto_control.windows.screen.screen import size

left = (LEFTUP, LEFTDOWN, 0)
middle = (MIDDLEUP, MIDDLEDOWN, 0)
right = (RIGHTUP, RIGHTDOWN, 0)
x1 = (XUP, XDOWN, XBUTTON1)
x2 = (XUP, XDOWN, XBUTTON2)

get_cursor_pos = windll.user32.GetCursorPos
set_cursor_pos = windll.user32.SetCursorPos


def position():
    point = wintypes.POINT()
    if get_cursor_pos(ctypes.byref(point)):
        return point.x, point.y
    else:
        return None


def set_position(pos):
    pos = int(pos[0]), int(pos[1])
    set_cursor_pos(*pos)


def press_mouse(pressButton):
    SendInput(1, ctypes.byref(
        Input(type=Mouse, _input=Input.INPUT_Union(
            mi=MouseInput(dwFlags=pressButton[1], mouseData=pressButton[2])))),
              ctypes.sizeof(Input))


def release_mouse(pressButton):
    SendInput(1, ctypes.byref(
        Input(type=Mouse, _input=Input.INPUT_Union(
            mi=MouseInput(dwFlags=pressButton[0], mouseData=pressButton[2])))),
              ctypes.sizeof(Input))


def scroll(wheel_value, x=None, y=None):
    now_cursor_x, now_cursor_y = position()
    width, height = size()
    if x is None:
        x = now_cursor_x
    else:
        if x < 0:
            x = 0
        elif x >= width:
            x = width - 1
    if y is None:
        y = now_cursor_y
    else:
        if y < 0:
            y = 0
        elif y >= height:
            y = height - 1
    mouse_event(WHEEL, x, y, dwData=wheel_value)

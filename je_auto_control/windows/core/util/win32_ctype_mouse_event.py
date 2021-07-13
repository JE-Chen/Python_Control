from je_auto_control.windows.core.util.win32_ctype_input import ctypes
from je_auto_control.windows.screen import size


def mouse_event(event, x, y, dwData=0):
    width, height = size()
    convertedX = 65536 * x // width + 1
    convertedY = 65536 * y // height + 1
    ctypes.windll.user32.mouse_event(event, ctypes.c_long(convertedX), ctypes.c_long(convertedY), dwData, 0)

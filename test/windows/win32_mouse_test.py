import time

from je_auto_control import win32_ctype_mouse_control as mouse_control
from je_auto_control.windows.mouse import win32_mouse_left
from je_auto_control.windows.mouse import win32_mouse_right

time.sleep(1)
print(mouse_control.position())
mouse_control.set_position(809, 388)
mouse_control.press_mouse(win32_mouse_right)
mouse_control.release_mouse(win32_mouse_right)
mouse_control.press_mouse(win32_mouse_left)
mouse_control.release_mouse(win32_mouse_left)

mouse_control.click_mouse(win32_mouse_left)

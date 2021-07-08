import time

from je_auto_control.windows.mouse import left
from je_auto_control.windows.mouse import right
from je_auto_control import win32_ctype_mouse_control as mouse_control

time.sleep(1)
print(mouse_control.position())
mouse_control.set_position((809, 388))
mouse_control.press_mouse(right)
mouse_control.release_mouse(right)
mouse_control.press_mouse(left)
mouse_control.release_mouse(left)

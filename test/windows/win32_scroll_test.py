import time

from je_auto_control import win32_ctype_mouse_control as mouse_control

time.sleep(3)
print(mouse_control.position())
mouse_control.scroll(500)

import time

from je_auto_control import x11_linux_mouse_control as linux_mouse

from je_auto_control import x11_linux_scroll_direction_down
from je_auto_control import x11_linux_scroll_direction_up

linux_mouse.scroll(5, x11_linux_scroll_direction_down)
time.sleep(1)
"""
this block just scroll test use








































"""
linux_mouse.scroll(5, x11_linux_scroll_direction_up)

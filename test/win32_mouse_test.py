from je_auto_control import win32_ctype_mouse_control
from je_auto_control.mouse.win32_ctype_mouse_control import right

print(win32_ctype_mouse_control.get_pos())
win32_ctype_mouse_control.set_pos((809, 388))
win32_ctype_mouse_control.press_mouse(right)
win32_ctype_mouse_control.release_mouse(right)

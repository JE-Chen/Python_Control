from je_auto_control import win32_ctype_mouse_control as mouse_control
from je_auto_control.mouse.win32_ctype_mouse_control import left
from je_auto_control.mouse.win32_ctype_mouse_control import right

print(mouse_control.get_pos())
mouse_control.set_pos((809, 388))
mouse_control.press_mouse(right)
mouse_control.release_mouse(right)
mouse_control.press_mouse(left)
mouse_control.release_mouse(left)

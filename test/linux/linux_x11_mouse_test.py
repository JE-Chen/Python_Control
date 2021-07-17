from je_auto_control import x11_linux_mouse_control as linux_mouse
from je_auto_control import x11_linux_mouse_right

print(linux_mouse.position())
linux_mouse.set_position(100, 100)
print(linux_mouse.position())
linux_mouse.click_mouse(x11_linux_mouse_right)

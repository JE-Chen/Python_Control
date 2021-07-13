from je_auto_control.linux_with_x11.mouse import x11_linux_mouse_control as linux_mouse

print(linux_mouse.position())
linux_mouse.set_position(100, 100)
from je_auto_control.linux_with_x11.core.x11_linux_display import display


def size():
    return display.screen().width_in_pixels, display.screen().height_in_pixels

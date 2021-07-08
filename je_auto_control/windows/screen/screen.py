import ctypes

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()


def size():
    return [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

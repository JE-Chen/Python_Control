from je_auto_control.core.util.win32_ctype_input \
    import (LEFTUP, LEFTDOWN, MIDDLEUP, MIDDLEDOWN, RIGHTUP, RIGHTDOWN, XUP, XDOWN, XBUTTON1, XBUTTON2, windll,
            wintypes, ctypes,
            Input, SendInput, Mouse, MouseInput, WHEEL)

left = (LEFTUP, LEFTDOWN, 0)
middle = (MIDDLEUP, MIDDLEDOWN, 0)
right = (RIGHTUP, RIGHTDOWN, 0)
x1 = (XUP, XDOWN, XBUTTON1)
x2 = (XUP, XDOWN, XBUTTON2)

wheelData = 120
getCursorPos = windll.user32.GetCursorPos
setCursorPos = windll.user32.SetCursorPos


def getPos():
    point = wintypes.POINT()
    if getCursorPos(ctypes.byref(point)):
        return (point.x, point.y)
    else:
        return None


def setPos(pos):
    pos = int(pos[0]), int(pos[1])
    setCursorPos(*pos)


def wheel(dx=None, dy=None):
    if dy:
        SendInput(
            1,
            ctypes.byref(Input(type=Mouse, _input=Input.INPUT_Union(
                mi=MouseInput(dwFlags=WHEEL, mouseData=int(dy * wheelData))))),
            ctypes.sizeof(Input))
    if dx:
        SendInput(
            1,
            ctypes.byref(Input(type=Mouse, _input=Input.INPUT_Union(
                mi=MouseInput(dwFlags=WHEEL, mouseData=int(dx * wheelData))))),
            ctypes.sizeof(Input))


def pressMouse(pressButton):
    SendInput(1, ctypes.byref(
        Input(type=Mouse, _input=Input.INPUT_Union(
            mi=MouseInput(dwFlags=pressButton[1], mouseData=pressButton[2])))),
              ctypes.sizeof(Input))


def releaseMouse(pressButton):
    SendInput(1, ctypes.byref(
        Input(type=Mouse, _input=Input.INPUT_Union(
            mi=MouseInput(dwFlags=pressButton[0], mouseData=pressButton[2])))),
              ctypes.sizeof(Input))

from JEAutoControl.Core.Util.Win32CtypeINPUT \
    import (LEFTUP,LEFTDOWN,MIDDLEUP,MIDDLEDOWN,RIGHTUP,RIGHTDOWN,XUP,XDOWN,XBUTTON1,XBUTTON2,windll,wintypes,ctypes,
            INPUT,SendInput,Mouse,MOUSEINPUT,WHEEL)


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
            ctypes.byref(INPUT(type=Mouse, _input=INPUT.INPUT_Union(
                mi=MOUSEINPUT(dwFlags=WHEEL, mouseData=int(dy * wheelData))))),
            ctypes.sizeof(INPUT))
    if dx:
        SendInput(
            1,
            ctypes.byref(INPUT(type=Mouse, _input=INPUT.INPUT_Union(
                mi=MOUSEINPUT(dwFlags=WHEEL, mouseData=int(dx * wheelData))))),
            ctypes.sizeof(INPUT))

def pressMouse(pressButton):
    SendInput(1, ctypes.byref(
        INPUT(type=Mouse, _input=INPUT.INPUT_Union(
            mi=MOUSEINPUT(dwFlags=pressButton[1], mouseData=pressButton[2])))),
              ctypes.sizeof(INPUT))

def releaseMouse(pressButton):
    SendInput(1, ctypes.byref(
        INPUT(type=Mouse, _input=INPUT.INPUT_Union(
            mi=MOUSEINPUT(dwFlags=pressButton[0], mouseData=pressButton[2])))),
              ctypes.sizeof(INPUT))



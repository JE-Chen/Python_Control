import enum

from Core.Util.Win32CtypeINPUT import *
from Core.Util.Win32VK import *


class CtypeMouseControl():
    class MouseButton(enum.Enum):
        unknown = None
        left = (LEFTUP, LEFTDOWN, 0)
        middle = (MIDDLEUP, MIDDLEDOWN, 0)
        right = (RIGHTUP, RIGHTDOWN, 0)
        x1 = (XUP, XDOWN, XBUTTON1)
        x2 = (XUP, XDOWN, XBUTTON2)

    class MouseControl():
        wheelData = 120
        getCursorPos = windll.user32.GetCursorPos
        setCursorPos = windll.user32.SetCursorPos

        def getPos(self):
            point = wintypes.POINT()
            if self.getCursorPos(ctypes.byref(point)):
                return (point.x, point.y)
            else:
                return None

        def setPos(self, pos):
            pos = int(pos[0]), int(pos[1])
            self.setCursorPos(*pos)

        def wheel(self, dx=None, dy=None):
            if dy:
                SendInput(
                    1,
                    ctypes.byref(INPUT(type=Mouse, _input=INPUT.INPUT_Union(
                        mi=MOUSEINPUT(dwFlags=WHEEL, mouseData=int(dy * self.wheelData))))),
                    ctypes.sizeof(INPUT))
            if dx:
                SendInput(
                    1,
                    ctypes.byref(INPUT(type=Mouse, _input=INPUT.INPUT_Union(
                        mi=MOUSEINPUT(dwFlags=WHEEL, mouseData=int(dx * self.wheelData))))),
                    ctypes.sizeof(INPUT))

        def pressMouse(self, pressButton):
            SendInput(1, ctypes.byref(
                INPUT(type=Mouse, _input=INPUT.INPUT_Union(
                    mi=MOUSEINPUT(dwFlags=pressButton.value[1], mouseData=pressButton.value[2])))),
                      ctypes.sizeof(INPUT))

        def releaseMouse(self, pressButton):
            SendInput(1, ctypes.byref(
                INPUT(type=Mouse, _input=INPUT.INPUT_Union(
                    mi=MOUSEINPUT(dwFlags=pressButton.value[0], mouseData=pressButton.value[2])))),
                      ctypes.sizeof(INPUT))


if __name__ == "__main__":
    test = CtypeMouseControl()
    print(test.MouseControl().getPos())
    test.MouseControl().setPos((1743, 46))
    test.MouseControl().setPos((800, 500))
    test.MouseControl().pressMouse(test.MouseButton.left)
    test.MouseControl().releaseMouse(test.MouseButton.left)
    test.MouseControl().wheel(120)

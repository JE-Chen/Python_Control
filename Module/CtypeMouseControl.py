import enum
from Core.Util.CtypeINPUT import *
from Core.Util.VK import *

class CtypeMouseControl():

    class MouseButton(enum.Enum):
        unknown = None
        left = (LEFTUP, LEFTDOWN, 0)
        middle = (MIDDLEUP, MIDDLEDOWN, 0)
        right = (RIGHTUP, RIGHTDOWN, 0)
        x1 = (XUP, XDOWN, XBUTTON1)
        x2 = (XUP, XDOWN, XBUTTON2)


    class MouseControl():
        getCursorPos = windll.user32.GetCursorPos
        setCursorPos = windll.user32.SetCursorPos

        def getPos(self):
            point = wintypes.POINT()
            if self.getCursorPos(ctypes.byref(point)):
                return (point.x,point.y)
            else :
                return None

if __name__ == "__main__":
    test = CtypeMouseControl.MouseControl()
    print(test.getPos())

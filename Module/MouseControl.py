import mouse

class MouseControl():

    def __init__(self):
        pass

    def click(self,button):
        mouse.click(button)

    def position(self):
        return mouse.get_position()

    def drag(self,x1 ,y1 ,x2 ,y2 ,absolute = True, duration = 0.1):
        mouse.drag(x1,y1,x2,y2,absolute,duration)

    def move(self,x,y,absolute = True , duration = 0.2):
        mouse.move(x,y,absolute,duration)

    def wheel(self,scrollValue):
        mouse.wheel(scrollValue)

    def onClick(self,function):
        mouse.on_click(lambda : function)

    def unhookAll(self):
        mouse.unhook_all()
import Quartz

from je_auto_control.osx.core.osx_vk import mouse_left
from je_auto_control.osx.core.osx_vk import mouse_middle
from je_auto_control.osx.core.osx_vk import mouse_right


def position():
    return (Quartz.NSEvent.mouseLocation().x, Quartz.NSEvent.mouseLocation().y)


def mouse_event(event,x ,y , mouse_button):
    curr_event = Quartz.CGEventCreateMouseEvent(None, event, (x, y), mouse_button)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, curr_event)


def set_position(x, y):
    mouse_event(Quartz.kCGEventMouseMoved, x, y, 0)


def press_mouse(x, y, mouse_type):
    if mouse_type is mouse_left:
        mouse_event(Quartz.kCGEventLeftMouseDown,x ,y,Quartz.kCGMouseButtonLeft)
    elif mouse_type is mouse_middle:
        mouse_event(Quartz.kCGEventOtherMouseDown,x ,y,Quartz.kCGMouseButtonCenter)
    elif mouse_type is mouse_right:
        mouse_event(Quartz.kCGEventRightMouseDown,x ,y,Quartz.kCGMouseButtonRight)


def release_mouse(x, y, mouse_type):
    if mouse_type is mouse_left:
        mouse_event(Quartz.kCGEventLeftMouseUp,x ,y,Quartz.kCGMouseButtonLeft)
    elif mouse_type is mouse_middle:
        mouse_event(Quartz.kCGEventOtherMouseUp,x ,y,Quartz.kCGMouseButtonCenter)
    elif mouse_type is mouse_right:
        mouse_event(Quartz.kCGEventRightMouseUp,x ,y,Quartz.kCGMouseButtonRight)

        
def click(x,y,mouse_type):
    if mouse_type is mouse_left:
        press_mouse(x,y,mouse_type)
        release_mouse(x,y,mouse_type)
    elif mouse_type is mouse_middle:
        press_mouse(x,y,mouse_middle)
        release_mouse(x,y,mouse_middle)
    elif mouse_type is mouse_right:
        press_mouse(x,y,mouse_right)
        release_mouse(x,y,mouse_right)





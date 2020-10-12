from Module.Win32CtypeKeyboardControl import CtypeKeyboardControl

class KeyboardCore():

    def __init__(self):
        try:
            self.CtypeKeyboardControl = CtypeKeyboardControl()
        except Exception as Errr:
            raise Errr
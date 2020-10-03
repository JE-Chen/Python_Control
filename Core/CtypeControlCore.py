from Module.CtypeKeyboardControl import CtypeKeyboardControl

class CtypeControlCore():

    def __init__(self):
        try:
            self.CtypeKeyboardControl=CtypeKeyboardControl()
        except Exception as Errr:
            raise Errr

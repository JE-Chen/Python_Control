import keyboard

class Addreviation():

    def __init__(self):
        pass

    def SetAbbreviation(self,source,replacestring):
        keyboard.add_abbreviation(source,replacestring)

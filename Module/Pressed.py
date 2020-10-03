import keyboard
import threading

class Pressed(threading.Thread):

    running = True

    def __init__(self):
        super().__init__()

    def run(self):
        while self.running:
            pass

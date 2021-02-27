import threading
from AutoHotPy import AutoHotPy

class App:
    def __init__(self, eel):
        self.eel = eel

        self.auto = AutoHotPy()
        self.startKL()

        self.counter = 0

    def startKL(self):
        self.threadKL = threading.Thread(target=self.keyboardListener)
        self.threadKL.start()

    def add1(self):
        self.counter += 1
        self.eel.setCounter(self.counter)

    def remove1(self):
        if self.counter>0:
            self.counter -= 1
            self.eel.setCounter(self.counter)

    def resetCounter(self):
            self.counter = 0
            self.eel.setCounter(self.counter)

    def keyboardListener(self):
        self.auto.registerExit(self.auto.I, lambda a,b:self.auto.stop())
        self.auto.registerForKeyDown(self.auto.P, lambda a, b : self.add1())
        self.auto.start()
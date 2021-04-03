import threading
from AutoHotPy import AutoHotPy
import tkinter as tk
import time
import psutil, win32process, win32gui
import os

class App:
    def __init__(self, eel):
        self.eel = eel
        self.auto = AutoHotPy()

        self.changingLK = False

        self.listenedKey = self.auto.P

        if os.path.exists("counter"):
            with open('counter', 'r') as f:
                try:
                    self.counter = int(f.read())
                except:
                    self.counter = 0
        else:
            with open('counter', 'w') as f:
                self.counter = 0
                f.write(str(self.counter))
        
        self.lockStartingKL = False
        self.startKL()

    def saveCounterToFile(self):
        with open('counter', 'w') as f:
            f.write(str(self.counter))

    def startKL(self):
        if self.lockStartingKL:
            return False
        self.threadKL = threading.Thread(target=self.keyboardListener)
        self.threadKL.start()

    def add1(self):
        self.counter += 1
        self.eel.setCounter(self.counter)

        self.saveCounterToFile()

    def remove1(self):
        if self.counter>0:
            self.counter -= 1
            self.eel.setCounter(self.counter)

            self.saveCounterToFile()

    def resetCounter(self):
        self.counter = 0
        self.eel.setCounter(self.counter)

        self.saveCounterToFile()

    def isGameActive(self):
        def active_window_process_name():
            pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow()) #This produces a list of PIDs active window relates to
            return psutil.Process(pid[-1]).name() #pid[-1] is the most likely to survive last longer
        return True if active_window_process_name() == "sekiro.exe" else False

    def keyboardListener(self):
        self.auto.stop()
        self.auto = AutoHotPy()
        self.auto.exit_configured = True

        self.listenedKey = self.auto.keys[self.listenedKey.get_id()]

        self.auto.registerForKeyDown(self.listenedKey, lambda a, b : self.add1() if self.isGameActive() else self.listenedKey.press())
        self.auto.start()

    def changeListenedKey(self):
        self.changingLK = True

        self.auto.stop()
        self.auto = AutoHotPy()
        self.auto.exit_configured = True

        def showDialog():
            dialog = tk.Tk()
            dialog.attributes("-topmost", True)
            tk.Label(text="Listening for new key...", padx=20, pady=20).pack()
            dialog.update()
            return dialog

        def keyPressed(a, e):
            self.auto.stop()
            for key in self.auto.keys.values():
                if key.code == e.code:
                    self.listenedKey = key
                    return

        for key in self.auto.keys.values():
            self.auto.registerForKeyDown(key, keyPressed)

        dialog = showDialog()
        self.auto.start()
        dialog.destroy()

        self.auto = AutoHotPy()
        self.auto.exit_configured = True
        self.startKL()

        self.changingLK = False

        return self.listenedKey.string_representation
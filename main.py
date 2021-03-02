import eel
import app
import time
import threading

eel.init('web')

app = app.App(eel)

@eel.expose
def getCounterValue():
    print("getCounterValue triggered")
    return app.counter

@eel.expose
def add1():
    print("add1 triggered")
    app.add1()

@eel.expose
def remove1():
    print("remove1 triggered")
    app.remove1()

@eel.expose
def resetCounter():
    print("resetCounter triggered")
    app.resetCounter()

@eel.expose
def checkKLThread():
    print("checkKLThread triggered")
    return app.threadKL.is_alive()

@eel.expose
def stopKL():
    print("stopKL triggered")
    app.auto.stop()

@eel.expose
def startKL():
    print("startKL triggered")
    if not checkKLThread():
        app.startKL()

@eel.expose
def changeLK():
    print("stopKL triggered")
    if not app.changingLK:
        return app.changeListenedKey()

eel.start('index.html', size=(400, 550))
import threading
from time import sleep

import pyttsx3

s = pyttsx3.init()
readingThread = threading.Thread()
continueReading = True
pauseReading = False

def __sayText(text):
    for word in text.split('.'):
        print(word)
        if len(word) > 0:
            s.say(word)
            s.runAndWait()
        global continueReading
        global pauseReading
        while pauseReading:
            sleep(1)
        if not continueReading:
            break;


def sayText(text):
    continueReading = True
    readingThread = threading.Thread(target=__sayText, args=(text, ))
    readingThread.start()

def togglePauseReading():
    global pauseReading
    pauseReading = not pauseReading

def stopReading():
    print('try to stop reading')
    global continueReading
    continueReading = False



def test():
    sayText("Иди в жопу, придурок!")

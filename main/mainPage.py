from tkinter import filedialog as fd, Button, mainloop, Tk
from tkinter.ttk import Label

from wordReader import reader as msWordReader;
from textCpeech import reader as textSpeecher;


def read(path):
    textSpeecher.sayText(msWordReader.reader(path))


def selectAndRead():
    filename = fd.askopenfilename()
    read(filename)


def stopReading():
    textSpeecher.stopReading()


def togglePause():
    textSpeecher.togglePauseReading()


master = Tk()
master.geometry("200x200")
label = Label(master,
              text="Читалка для MSWord файлов")
label.pack(pady=10)

btn = Button(master,
             text="Выбрать файл *.docx",
             command=selectAndRead)
btn.pack(pady=10)

pauseBnt = Button(master,
                 text="Пауза",
                 command=togglePause)
pauseBnt.pack(pady=10)

stopBnt = Button(master,
                 text="Остановить",
                 command=stopReading)
stopBnt.pack(pady=10)

mainloop()




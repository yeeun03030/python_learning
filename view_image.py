from tkinter import *
from time import *

import main as M

def PrevImage():
    global num
    fnameList = ['%s_%d'%(M.name, i) for i in range(1, 80)]

    window = Tk()
    window.geometry("700x500")
    window.title("사진 앨범 보기")
    
    btnPrev = Button(window, text = "<", command = clickPrev(name, pLabel, fnameList))
    btnNext = Button(window, text = ">", command = clickNext(name, pLabel, fnameList))

    photo = PhotoImage(file='D:/miniProject/ImgDir/%s/%s.jpg' % (name, fnameList[0]))

    pLabel = Label(window, image=photo)

    btnPrev.place(x = 0, y = 250)
    btnNext.place(x = 700, y = 250)

def clickNext(name, pLabel, fnameList):
    global num

    num += 1
    if num > 79:
        num = 0
    photo = PhotoImage(file='D:/miniProject/ImgDir/%s/%s.jpg' % (name, fnameList[num]))

    return photo

def clickPrev(name, pLabel, fnameList):
    global num

    num -= 1
    if num < 0:
        num = 79
    photo = PhotoImage(file='D:/miniProject/ImgDir/%s/%s.jpg' % (name, fnameList[num]))

    return photo

num = 0
photoList = [None] * 80

if __name__ == "__main__":
   

    PrevImage(M.name)

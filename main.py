from tkinter import *
from tkinter.simpledialog import *
from tkinter.filedialog import *
from tkinter import messagebox
import os.path
import string
import private_to as pt

import view_image as vi
from PIL import Image, ImageTk

def func_search(name = None):
    if name == None :
        name = askstring("Add famous person", "추가할 인물의 이름을 입력하세요.")
        name = name.replace(" ", "")
        name = name.translate(str.maketrans('', '', string.punctuation))

        if name == "" :
            messagebox.showerror("Error", "제대로 입력해주세요.")
            return 

    if os.path.isdir('D:/miniProject/ImgDir/%s'%(name)):
        messagebox.showerror("Error", "동일한 인물 디렉토리가 존재합니다. 재검색하세요.")

    else :
        messagebox.showinfo("Success", "[%s] 디렉토리가 생성되었습니다."%(name))
        os.mkdir('D:/miniProject/ImgDir/%s/'%(name)) 

        pt.search_name(name)

def func_open():
    global basewidth, baseheight
    filePath = askopenfilename(parent=window, filetypes=(("모든 그림 파일", "*.jpg;*.jpeg;*.bmp;*.png;*.tif;*.gif"),  ("모든 파일", "*.*") ))

    if filePath :
        global xSize, ySize

        image = Image.open(filePath)
        photo = ImageTk.PhotoImage(image)
        xSize = photo.width()
        ySize = photo.height()
        
        window.geometry("%dx%d"%(xSize, ySize))

        img_label.config(image=photo)
        img_label.image = photo

def func_image_viewer():
    global name

    name = askstring("Viewer", "사진을 볼 인물의 이름을 입력하세요.")
    name = name.replace(" ", "")
    name = name.translate(str.maketrans('', '', string.punctuation))

    if name == "" :
        messagebox.showerror("Error", "제대로 입력해주세요.")
        return 

    if os.path.isdir('D:/miniProject/ImgDir/%s/'%(name)):
        vi.PrevImage()

    else:
        chk = messagebox.askokcancel(title='Error', message="이 인물의 디렉토리가 없습니다. 생성하시겠습니까?")
        
        if chk:
            func_search(name)

def func_exit():
    exit()

name = None
window = None
photo = None
pLabel = None
basewidth = 500
xSize, ySize = 600, 700

if __name__ == "__main__":
    if os.path.isdir('D:/miniProject') == False :
        os.mkdir('D:/miniProject/')
        os.mkdir('D:/miniProject/ImgDir/')

    window = Tk()

    mainMenu = Menu(window)
    window.config(menu = mainMenu)

    window.title("Image Search & Viewer Program")
    window.geometry("%dx%d"%(xSize, ySize))
    window.resizable(0,0)

    img_label = Label(window)
    img_label.pack(expand = 1, anchor = CENTER)

    fileMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label="Search", command=func_search)
    fileMenu.add_command(label="Open_view", command=func_open)
    fileMenu.add_command(label="Image_view", command=func_image_viewer)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=func_exit)

    window.mainloop()

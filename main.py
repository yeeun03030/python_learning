from tkinter import *
from tkinter.simpledialog import *
# from tkinter.filedialog import *
from tkinter import messagebox
import pillow_use as pu
import os.path
import string

import img_download as ImgD

def func_search():
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

        ImgD.search_image(name)
'''
def func_image_viewer():
    name = askstring("Viewer", "사진을 볼 인물의 이름을 입력하세요.")
    name = name.replace(" ", "")
    name = name.translate(str.maketrans('', '', string.punctuation))

    if name == "" :
        messagebox.showerror("Error", "제대로 입력해주세요.")
        return 

    if os.path.isdir('D:/miniProject/ImgDir/%s'%(name)):
        
'''


def func_exit():
    exit()


if __name__ == "__main__":
    if os.path.isdir('D:/miniProject') == False :
        os.mkdir('D:/miniProject/')
        os.mkdir('D:/miniProject/ImgDir/')

    window = Tk()

    mainMenu = Menu(window)
    window.config(menu = mainMenu)

    window.title("Image Search Program")
    window.geometry("400x300")
    window.resizable(0,0)

    fileMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label="Search", command=func_search)
    fileMenu.add_command(label="Image_view")
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=func_exit)

    window.mainloop()
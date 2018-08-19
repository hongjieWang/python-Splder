# -*- coding:utf-8 -*-
from tkinter import *
import tkinter as tk
from cn.org.whj.ai.day_two.Mouse import Mouse
from PIL import Image, ImageTk
from cn.org.whj.ai.day_one.handwriting_recognition import Recognition
from cn.org.whj.ai.day_two.ImageUtils import changeImage28
import os


def creat_image():
    mn = Mouse()
    mn.create_image()


class App(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        root.title('手写识别')
        w = Canvas(root, width=500, height=20)
        w.pack()

        Label(root, text='欢迎使用手写识别系统，以下为使用说明').pack(side=TOP)
        Label(root, text='1、点击生成手写图片按钮，摁下m切换到手写状态，点击鼠标左键，进行手写操作。').pack(side=TOP, anchor=W)
        Label(root, text='2、手写✅后，摁下w进行切图操作，点击鼠标左键，选择截取数字区域').pack(side=TOP, anchor=W)
        Label(root, text='3、点击刷新按钮，回显截图').pack(side=TOP, anchor=W)
        Label(root, text='4、点击数字识别按钮，识别截图中数字(0~9)').pack(side=TOP, anchor=W)
        Label(root, text='识别到数字是：').pack(side=TOP, anchor=W)
        self.numLabel = Label(root, text='', relief=RAISED,fg="red", font=("黑体", 30, "bold"))
        self.numLabel.pack(side=TOP, anchor=CENTER)
        Label(root, text='').pack(side=TOP, anchor=W)

        fm = Frame(root)
        # Button是一种按钮组件，与Label类似，只是多出了响应点击的功能
        Button(fm, text='生成手写图片', command=creat_image).pack(side=TOP, anchor=W, fill=X, expand=YES)
        Button(fm, text='刷新', command=self.changeImage).pack(side=TOP, anchor=W, fill=X, expand=YES)
        Button(fm, text='数字识别', command=self.recognition).pack(side=TOP, anchor=W, fill=X, expand=YES)
        Button(fm, text='汉字识别').pack(side=TOP, anchor=W, fill=X, expand=YES)

        fm.pack(side=LEFT, fill=BOTH, expand=YES, padx=20)

        self.pilImage = Image.open("only.png")
        self.tkImage = ImageTk.PhotoImage(image=self.pilImage)
        self.label = Label(root, image=self.tkImage)
        self.label.pack()

        Label(root, text="按住鼠标左键并移动，开始绘制你的理想蓝图吧......").pack(side=BOTTOM)

    def changeImage(self):
        self.png = tk.PhotoImage(file="only.png")  # 需要储存为实例属性，否则会被垃圾回收
        self.label.configure(image=self.png)

    def recognition(self):
        base_dir = os.path.dirname(os.getcwd())
        re = Recognition(base_dir)
        img = Image.open('only.png')
        img = changeImage28(img)
        results = re.readImage2result(rimg=img)
        self.numLabel.configure(text=str(results))


if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()

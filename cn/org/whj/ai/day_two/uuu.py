# coding=utf-8
import tkinter as tk
import os


class RuKou(tk.Frame):
    """
    登入的入口
    将要做成运行时显示接口所返回的图片并展示
    """

    def __init__(self, master=None):
        """
        在这里展示一个图片，初步设想是
        运行时，登入接口
        把其返回的图片显示在此处
        """
        super().__init__(master)
        self.pack()
        self.createWidgets()  # 用这个方法创建一个组件，这个组件就是用来显示登陆png的
        self.lab1 = tk.Label(self)
        self.lab1.pack()

    def createWidgets(self):
        """
        这里调用diaoYong方法和showPng方法
        进行登陆，首先出现一个登入按钮，点击按钮，然后调用diaoYong()
        才会返回一个图片的路径
        """
        self.login = tk.Button(self, text="登入", command=self.diaoYong)
        self.login.pack(side="top")

    def diaoYong(self):
        """
        返回登入用的图片路径
        """

        self.showPng("only.png")

    def showPng(self, pngPath):
        """
        展示图片
        """
        self.png = tk.PhotoImage(file=pngPath)  # 需要储存为实例属性，否则会被垃圾回收
        self.lab1.configure(image=self.png)  ##


root = tk.Tk()
# 进入消息循环
app = RuKou(master=root)
root.mainloop()

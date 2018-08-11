# -*- coding:utf-8 -*-
import os
from tkinter import *
from tkinter import messagebox
from cn.org.whj.face.photograph import photo_graph
from cn.org.whj.face.image_utils import ImageUtils
from PIL import Image, ImageTk


class FaceUI(Tk, object):
    def __init__(self):
        super(FaceUI, self).__init__()
        self.title("欢迎使用人脸识别管理系统")
        self.geometry('700x400')
        self.face_name = StringVar()
        self.face_path = StringVar()
        self.show_face_path = ''
        self.add_label()

    def add_label(self):
        w = Label(self, text="请输入待检测人姓名：")
        w.grid(row=0)
        self.face_name.set('')
        en = Entry(self, textvariable=self.face_name)
        en.grid(row=0, column=1)
        btn = Button(self, text="确认信息", command=self.btn_name)
        btn.grid(row=0, column=2)
        w = Label(self, text="请输入存储路径：")
        w.grid(row=1)
        self.face_path.set('/Users/wanghongjie/PycharmProjects/lp/tempImage/wanghongjie')
        en = Entry(self, textvariable=self.face_path)
        en.grid(row=1, column=1)
        btn = Button(self, text="检查路径", command=self.cheak_path)
        btn.grid(row=1, column=2)
        btn = Button(self, text="拍照", command=self.photograph)
        btn.grid(row=2)

        btn = Button(self, text="清除", command=self.remove_dir)
        btn.grid(row=2, column=1)

    def btn_name(self):
        messagebox.showinfo(title='用户信息确认：', message="userName is " + self.face_name.get())
        print("获取文本框信息为：" + self.face_name.get())

    def cheak_path(self):
        print("存储路径为：" + self.face_path.get())
        path = self.face_path.get()
        self.mkdir(path)

    def photograph(self):
        print("照相")
        ph = photo_graph()
        path = ph.face(self.face_path.get() + "/" + self.face_name.get() + ".png")
        self.show_photo(path)

    def show_photo(self, path):
        size, bm = ImageUtils().img_magnification(path)
        bm = ImageTk.PhotoImage(bm)
        label2 = Label(self, image=bm, width=640, height=360)
        label2.bm = bm
        label2.grid(row=3, columnspan=3)

    def mkdir(self, path):
        # 去除首位空格
        path = path.strip()
        # 去除尾部 / 符号
        path = path.rstrip("/")

        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists = os.path.exists(path)

        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)
            print(path + ' 创建成功')
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print(path + ' 目录已存在')
            return False

    def remove_dir(self, path):
        if path is None:
            path = self.face_path.get()
        path = path.replace('\\', '/')
        if os.path.isdir(path):
            for p in os.listdir(path):
                self.remove_dir(os.path.join(path, p))
            if os.path.exists(path):
                os.rmdir(path)
        else:
            if os.path.exists(path):
                os.remove(path)


if __name__ == '__main__':
    env = FaceUI()
    env.mainloop()

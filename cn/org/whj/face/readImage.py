# -*- coding:utf-8 -*-

import os
import face_recognition


# 获取输入路径下所有文件
def all_path(dirname, filter):
    result = []  # 所有的文件
    file_name = []  # 所有文件名称
    for maindir, subdir, file_name_list in os.walk(dirname):
        # print("1:",maindir) #当前主目录
        # print("2:",subdir) #当前主目录下的所有目录
        # print("3:",file_name_list)  #当前主目录下的所有文件
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)  # 合并成一个完整路径
            ext = os.path.splitext(apath)[1]  # 获取文件后缀 [0]获取的是除了文件名以外的内容
            if ext in filter:
                result.append(apath)
                file_name.append(filename)
    return result, file_name


def all_file_name(dirname, filter):
    result = []  # 所有的文件
    file_name = []  # 所有文件名称不带后缀
    for maindir, subdir, file_name_list in os.walk(dirname):
        print("1:",maindir) #当前主目录
        print("2:", subdir)  # 当前主目录下的所有目录
        print("3:",file_name_list)  #当前主目录下的所有文件
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)  # 合并成一个完整路径
            print("4",os.path.basename(maindir))
            ext = os.path.splitext(apath)[1]  # 获取文件后缀 [0]获取的是除了文件名以外的内容
            if ext in filter:
                result.append(apath)
                file_name.append(filename.split(".", 1)[0])
    return result, file_name


def all_image_name(dirname, filter):
    known_face_encodings = []
    filepaths, names = all_file_name(dirname, filter)
    known_face_names = names
    for filepath in filepaths:
        _image = face_recognition.load_image_file(filepath)
        _face_encoding = face_recognition.face_encodings(_image)[0]
        known_face_encodings.append(_face_encoding)
    return known_face_encodings, known_face_names


if __name__ == '__main__':
    ww = [".png"]
    result, filename = all_file_name("/Users/wanghongjie/Downloads", ww)
    print(filename)
    print(result)

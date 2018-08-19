# -*- coding:utf-8 -*-
"""
Image converter utilities
"""


def changeImage28(img):
    out = img.resize((28, 28))  # resize成128*128像素大小。
    return out

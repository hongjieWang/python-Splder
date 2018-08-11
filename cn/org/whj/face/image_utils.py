

#coding=utf-8
from PIL import Image
import os


class ImageUtils(object):
    def __init__(self):
        super(ImageUtils, self).__init__()

    def img_magnification(self, path):
        img = Image.open(path)
        if img is None:
            print("Error: could not load image")
            os._exit(0)

        height, width = img.size
        # 缩小图像
        size = (int(height * 0.5), int(width * 0.5))
        img = img.resize(size, Image.ANTIALIAS)
        return size, img


if __name__ == '__main__':
    env = ImageUtils()
    env.img_magnification("/Users/wanghongjie/PycharmProjects/lp/tempImage/2121.png")

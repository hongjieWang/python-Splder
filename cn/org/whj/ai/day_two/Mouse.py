# -*- coding:utf-8 -*-
"""
Write the number generator, first, into the tablet, which is set to interfere with the picture,
press the m key, the handwritten number. Second, after the handwritten number is completed,
press the w key on the keyboard and perform the screenshot operation.
Drag the screenshot area with the left mouse button, and save the screenshot information automatically after release.
Finally, press q on the keyboard and exit the script
"""
import numpy as np
import cv2 as cv

drawing = False  # true if mouse is pressed
mode = True  # if True, draw rectangle. Press 'm' to toggle to curve
ix, iy = -1, -1


class Mouse():

    # mouse callback function
    def __init__(self):
        self.img = np.zeros((200, 200, 3), np.uint8)

    def draw_circle(self, event, x, y, flags, param):
        global ix, iy, drawing, mode
        if event == cv.EVENT_LBUTTONDOWN:
            drawing = True
            ix, iy = x, y
        elif event == cv.EVENT_MOUSEMOVE:
            if drawing:
                if self.mode:
                    cv.rectangle(self.img, (ix, iy), (x, y), (0, 255, 0), -1)
                else:
                    cv.circle(self.img, (x, y), 5, (0, 0, 255), -1)
        elif event == cv.EVENT_LBUTTONUP:
            drawing = False
            if self.mode:
                cv.rectangle(self.img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv.circle(self.img, (x, y), 5, (0, 0, 255), -1)

    def on_mouse(self, event, x, y, flags, param):
        global img, point1, point2
        img2 = self.img.copy()
        if event == cv.EVENT_LBUTTONDOWN:  # 左键点击
            point1 = (x, y)
            cv.circle(img2, point1, 10, (0, 255, 0), 5)
            cv.imshow('Digital writing pad', img2)
        elif event == cv.EVENT_MOUSEMOVE and (flags & cv.EVENT_FLAG_LBUTTON):  # 按住左键拖曳
            cv.rectangle(img2, point1, (x, y), (255, 0, 0), 5)
            cv.imshow('Digital writing pad', img2)
        elif event == cv.EVENT_LBUTTONUP:  # 左键释放
            point2 = (x, y)
            cv.rectangle(img2, point1, point2, (0, 0, 255), 5)
            cv.imshow('Digital writing pad', img2)
            min_x = min(point1[0], point2[0])
            min_y = min(point1[1], point2[1])
            width = abs(point1[0] - point2[0])
            height = abs(point1[1] - point2[1])
            cut_img = self.img[min_y:min_y + height, min_x:min_x + width]
            cv.imwrite('only.png', cut_img)

    def create_image(self):
        self.mode = True
        cv.namedWindow('Digital writing pad')
        cv.setMouseCallback('Digital writing pad', self.draw_circle)
        while (1):
            cv.imshow('Digital writing pad', self.img)
            k = cv.waitKey(1) & 0xFF
            if k == ord('m'):
                self.mode = not mode
            elif k == 27:
                break
            elif k == ord('w'):
                cv.setMouseCallback('Digital writing pad', self.on_mouse)
            elif k == ord('q'):
                break
        cv.destroyAllWindows()


if __name__ == '__main__':
    mn = Mouse()
    mn.create_image()

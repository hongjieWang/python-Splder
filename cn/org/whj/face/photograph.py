import cv2


class photo_graph(object):
    def __init__(self):
        super(photo_graph,self).__init__()

    def face(self, path):
        cap = cv2.VideoCapture(0)
        while (1):
            # get a frame
            ret, frame = cap.read()
            # show a frame
            cv2.imshow("capture", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.imwrite(path, frame)
                break
        cap.release()
        cv2.destroyAllWindows()
        return path


if __name__ == "__main__":
    env = photo_graph()
    env.face("")

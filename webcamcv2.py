"""
Simply display the contents of the webcam with optional mirroring using OpenCV 
via the new Pythonic cv2 interface.  Press <esc> to quit.
"""

import cv2
import time

def show_webcam():
    cam = cv2.VideoCapture(0)
    frame = 0
    while True:
#        if frame > 0:
#            onion = img.copy()
#            print "onion {} ".format(id(onion)),
        ret_val, img = cam.read()
#        img = cv2.flip(img.copy(), 1)
        print "cam {} ".format(id(img)),
        if frame > 0:
            view = cv2.addWeighted( onion, 0.5, img, 0.5, 0)
            print "view {} ".format(id(view))
            cv2.imshow('my webcam', view)
        else:
            cv2.imshow('my webcam', img)
            print "img {} ".format(id(img))
        key = cv2.waitKey(1) 
        if key == 27: 
            break  # esc to quit
        elif key == 32: 
            cv2.imwrite("frame%03d.png"%frame, img)
            onion = img.copy()
            print "onion {} ".format(id(onion)),
#            if frame > 0:
#                cv2.imwrite("view%03d.png"%frame, view)
#                cv2.imwrite("onione%03d.png"%frame, onion)
            frame += 1
#        time.sleep(1)
    cv2.destroyAllWindows()


def main():
    show_webcam()


if __name__ == '__main__':
    main()

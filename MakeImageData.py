import numpy as np
import cv2
import os

def captureImage():
    path_image = 5
    countImg = 0
    cap = cv2.VideoCapture(0)
    path = "/home/thaiduong/Desktop/FingerCalculator/" + str(path_image)
    os.mkdir(path)
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        cv2.rectangle(frame, (200, 100), (500, 400), (12, 255, 142), 1)
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame', gray)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('c'):
            print("c was pressed " + str(countImg))
            resizeImage(gray, path, countImg)
            countImg += 1
            print("image "+str(countImg-1)+" was saved")
        if key == ord('q'):
            break

    # for i in range(0, len(frames)):
    #     cv2.imwrite("pic"+str(i)+".jpg", frames[i])
    #     print("Pic"+str(i)+" was saved!")

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def resizeImage(img, path, count):
    cropImg = img[103:397, 203:497]
    resizeImg = cv2.resize(cropImg, (128, 128))
    cv2.imwrite(os.path.join(path, "pic" + str(count) + ".jpg"), resizeImg)

captureImage()
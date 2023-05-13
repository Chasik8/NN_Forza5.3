import torch
import numpy as np
import pyautogui
import cv2
def Train_init():
    file_kol=0
    vid_capture = cv2.VideoCapture(f'out{str(file_kol)}.avi')
    file_count = 0
    x_train=[]
    while (vid_capture.isOpened()):
        # Метод vid_capture.read() возвращают кортеж, первым элементом является логическое значение
        # а вторым кадр
        ret, frame = vid_capture.read()
        if ret == True:
            file_count += 1
            x_train.append(frame)
        else:
            break
    print(file_count)
    f=open(f'inp{str(file_kol)}.txt','r')
    y_train=list(map(str,f.read().split()))
    f.close()

def Train():
    pass
def Run():
    gz=float(60)
    size = (1902, 1080)
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.resize(frame, dsize=size, interpolation=cv2.INTER_CUBIC)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

def main():
    pass
if __name__=='__main__':
    main()
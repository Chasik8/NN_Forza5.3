import time

import cv2
import numpy as np
import pyautogui
import keyboard

# 60 30 20 10 15
def run_inp():
    # gz = float(input("Введи свою герцовку"))
    gz=float(15)
    k = 0
    try:
        ff = open('conf_drag.txt', 'r')
        k = int(ff.read())
        ff.close()
        ff = open('conf_drag.txt', 'w')
        ff.write(str(k + 1))
        ff.close()
    except:
        ff = open('conf_drag.txt', 'w')
        ff.write(str(0))
        ff.close()
    size = (1902, 1080)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(f"out_drag{str(k)}.avi", fourcc, gz, (size))
    f = open(f'inp_drag{str(k)}.txt', 'w')
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.resize(frame, dsize=size, interpolation=cv2.INTER_CUBIC)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        if keyboard.is_pressed('e'):
            f.write('e')
        elif keyboard.is_pressed('q'):
            f.write('q-')
        elif keyboard.is_pressed('-'):
            break
        else:
            f.write('_')
    f.close()


def run_out():
    vid_capture = cv2.VideoCapture('out_drag0.avi')
    file_count = 0
    while (vid_capture.isOpened()):
        # Метод vid_capture.read() возвращают кортеж, первым элементом является логическое значение
        # а вторым кадр
        ret, frame = vid_capture.read()
        if ret == True:
            # cv2.imshow('Look', frame)
            file_count += 1
            # print('Кадр {0:04d}'.format(file_count))
        else:
            break
    print(file_count)


def main():
    time.sleep(5)
    run_inp()
    # run_out()


if __name__ == '__main__':
    main()

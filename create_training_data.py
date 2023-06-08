import keyboard
import numpy

from getkeys import *
from grabscreen import *


def run():
    h = True
    k = 0
    try:
        ff = open('conf.txt', 'r')
        k = int(ff.read())
        ff.close()
        ff = open('conf.txt', 'w')
        ff.write(str(k + 1))
        ff.close()
    except:
        ff = open('conf.txt', 'w')
        ff.write(str(0))
        ff.close()
    file_name = f"train\out{str(k)}"
    h = False
    # training_data = []
    tim = time.time()
    save_kol = 60 * 10
    training_screen = []
    training_output = []
    while not h:
        # 800x600 windowed mode
        # screen = grab_screen(region=(0, 40, 800, 640))
        screen = grab_screen()
        # screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        # resize to something a bit more acceptable for a CNN
        # screen = cv2.resize(screen, (80, 60))
        keys = key_check()
        output = keys_to_output(keys)
        # output = keys
        # training_data.append([screen, output])
        training_screen.append(screen)
        training_output.append(output)
        # if cv2.waitKey(25) & 0xFF == ord('q'):
        if keyboard.is_pressed('-'):
            cv2.destroyAllWindows()
            h = True
        if len(training_screen) % save_kol == 0 or h:
            # if h:
            # print(len(training_data))
            # np.save(file_name, training_data)
            np.savez(file_name, a=training_screen, b=training_output)
            print(save_kol / (time.time() - tim))
            tim = time.time()
    # size = (1902, 1080)
    # fourcc = cv2.VideoWriter_fourcc(*"XVID")
    # out = cv2.VideoWriter(f"out{str(k)}.avi", fourcc, size=(size))
    # f = open(f'inp{str(k)}.txt', 'w')
    # while h:
    #     # надо вставить окно [0,0,1920,1080]
    #     sc = grab_screen()
    #     out.write(sc)-
    #     keys = key_check()
    #     f.write(str(keys))
    # f.close()


if __name__ == '__main__':
    run()

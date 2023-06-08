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
    file_name = f"train\out{str(k)}.npy"
    h = False
    training_data = []
    tim=time.time()
    save_kol=500
    while not h:
        # 800x600 windowed mode
        screen = grab_screen(region=(0, 40, 800, 640))
        last_time = time.time()
        # screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        # resize to something a bit more acceptable for a CNN
        screen = cv2.resize(screen, (80, 60))
        keys = key_check()
        output = keys_to_output(keys)
        # output = keys
        training_data.append([screen, output])
        # if cv2.waitKey(25) & 0xFF == ord('q'):
        if keyboard.is_pressed('-'):
            cv2.destroyAllWindows()
            h = True
        if len(training_data) % save_kol == 0 or h:
        # if h:
            print(len(training_data))
            np.save(file_name, training_data)
            print(save_kol/(time.time()-tim))
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

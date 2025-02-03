import time

import torch
import numpy as np
import pyautogui
import cv2
from model import *
from getkeys import *
from grabscreen import *
from directkeys import *

world = {
    1: 0x11,
    2: 0x20,
    3: 0x1F,
    4: 0x1E,
}


def Run():
    dev = torch.device("cuda:0")
    net = Net3()
    PATH = "models\model3.pth"
    net.load_state_dict(torch.load(PATH))
    net.eval()
    net.to(dev)
    h = True
    kol = 0
    while h:
        screen = grab_screen()
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        # resize to something a bit more acceptable for a CNN
        screen = cv2.resize(screen, (800, 600))
        screen = np.expand_dims(screen, axis=0)
        screen = torch.from_numpy(screen.astype(np.float32))
        screen = screen.to(device=dev)
        out = net(screen)
        out = out.detach().cpu().numpy()
        mi = 100000000000000
        mii = 0
        k = 0
        for i in out:
            if mi < i:
                mii = k
                mi=i
            k += 1
        if mii != 0:
            PressKey(world[mii])
        if kol == 10:
            h = False
        kol += 1


def main():
    Run()


if __name__ == '__main__':
    main()
#

import time

import torch
import numpy as np
import pyautogui
import cv2
from model import *
from tqdm import tqdm


def main():
    k = 0
    btach = 500
    file_name = f"train\out{str(k)}.npz"
    data = np.load(file_name)
    x_train = data['a'][:btach]
    y_train = data['b'][:btach]
    # np.save("colab\\out0_0a.npy",x_train)
    # np.save("colab\\out0_0b.npy", y_train)
    np.savez("colab\\out0_12.npz", a=x_train, b=y_train)


if __name__ == '__main__':
    main()

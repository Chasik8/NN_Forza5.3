import time

import torch
import numpy as np
import pyautogui
import cv2
from model import *
from tqdm import tqdm


def Train_init():
    k = 0
    btach = 500
    file_name = f"train\out{str(k)}.npz"
    data = np.load(file_name)
    x_train = data['a']
    y_train = data['b']
    # for img,out in data:
    #     x_train.append(img)
    #     y_train.append(out)
    # x_train=x_train[:btach]
    # y_train = y_train[:btach]
    x_train = np.expand_dims(x_train, axis=1)
    x_train = torch.from_numpy(x_train.astype(np.float32))
    y_train = torch.from_numpy(y_train.astype(np.float32))
    return x_train, y_train


def Train():
    pass


def Run():
    k_model = 0
    train_dop = True
    try:
        ff = open('conf_model.txt', 'r')
        k_model = int(ff.read())
        ff.close()
        ff = open('conf_model.txt', 'w')
        ff.write(str(k_model + 1))
        ff.close()
    except:
        ff = open('conf_model.txt', 'w')
        ff.write(str(1))
        ff.close()
    dev = torch.device("cuda:0")
    net = Net3()
    if train_dop:
        PATH = f"models\model{str(k_model - 1)}.pth"
        net.load_state_dict(torch.load(PATH))
        net.eval()
    net.to(dev)
    # net.cuda()
    x_train, y_train = Train_init()
    x_train = x_train.to(device=dev)
    y_train = y_train.to(device=dev)
    # x_train.cuda()
    # y_train.cuda()
    # criterion = nn.CrossEntropyLoss(size_average=None, reduce=None, reduction='mean')
    criterion = nn.MSELoss(size_average=None, reduce=None, reduction='mean')
    optimizer = torch.optim.Adam(net.parameters(), lr=0.0001)
    epoch_tim = time.time()
    print("Run")
    loss_max = 1000000000000000000000000
    if train_dop:
        ft = open(f"floss_dir\\floss_max.txt", 'r')
        loss_max = float(ft.read())
        ft.close()
    for epoch in range(net.num_epochs):
        # for i, (images, labels) in enumerate(train_loader):  # Загрузка партии изображений с индексом, данными,
        # классом
        loss = 0
        sr_loss = 0
        for i in tqdm(range(len(x_train))):
            # images = Variable(images.view(-1, 28 * 28))  # Конвертация тензора в переменную: изменяем изображение с
            # вектора, размером 784 на матрицу 28 x 28 labels = Variable(labels)
            optimizer.zero_grad()  # Инициализация скрытых масс до нулей
            outputs = net(x_train[i])  # Передний пропуск: определение выходного класса, данного изображения
            loss = criterion(outputs, y_train[i])  # Определение потерь: разница между выходным классом и предварительно
            # заданной
            # меткой
            loss.backward()
            # torch.cuda.empty_cache()  # Обратный проход: определение параметра weight
            optimizer.step()
            sr_loss += loss.item()
        print(epoch, sr_loss / len(x_train))
        if sr_loss / len(x_train) < loss_max:
            loss_max = sr_loss / len(x_train)
            torch.save(net.state_dict(), fr"models\model{k_model}_max.pth")
            floss_max = open("floss_max.txt", 'w')
            floss_max.write(str(sr_loss / len(x_train)))
            floss_max.close()
        if epoch % 10 == 0:
            torch.save(net.state_dict(), fr"models\model{k_model}.pth")
    torch.save(net.state_dict(), fr"models\model{k_model}.pth")
    print(time.time() - epoch_tim, (time.time() - epoch_tim) / net.num_epochs)


def main():
    Run()


if __name__ == '__main__':
    main()
#

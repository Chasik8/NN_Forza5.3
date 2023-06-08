import torch
import numpy as np
import pyautogui
import cv2
from model import *


def Train_init(dev):
    k = 0
    file_name = f"train\out{str(k)}.npz"
    data = np.load(file_name)
    x_train = data['a']
    y_train = data['b']
    # for img,out in data:
    #     x_train.append(img)
    #     y_train.append(out)
    x_train = torch.from_numpy(x_train.astype(np.float32)).to(dev)
    y_train = torch.from_numpy(y_train.astype(np.float32)).to(dev)
    return x_train, y_train


def Train():
    pass


def Run():
    k_model = 0
    try:
        ff = open('conf_model.txt', 'r')
        k_model = int(ff.read())
        ff.close()
        ff = open('conf_model.txt', 'w')
        ff.write(str(k_model + 1))
        ff.close()
    except:
        ff = open('conf_model.txt', 'w')
        ff.write(str(0))
        ff.close()
    dev = 'cuda:0'
    net = Net()
    net.to(dev)
    x_train, y_train = Train_init(dev)
    criterion = nn.MSELoss(size_average=None, reduce=None, reduction='mean')
    optimizer = torch.optim.Adam(net.parameters())
    for epoch in range(net.num_epochs):
        # for i, (images, labels) in enumerate(train_loader):  # Загрузка партии изображений с индексом, данными,
        # классом
        loss = 0
        for i in range(len(x_train)):
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
        print(epoch, loss.data)
    torch.save(net.state_dict(), fr"models\model{k_model}.pth")
def main():
    Run()


if __name__ == '__main__':
    main()
#

from torch import nn
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.l1=nn.Linear(1000,500)
        self.l2=nn.Linear(500,100)
        self.l3=nn.Linear(100,32)
        self.relu=nn.ReLU()
        self.sig=nn.Sigmoid()
    def forward(self, x):
        x=self.l1(x)
        x=self.relu(x)
        x = self.l2(x)
        x=self.relu(x)
        x = self.l3(x)
        x=self.sig(x)
        return x
import torch
from torch.optim import SGD
xs = torch.Tensor([0,1,2,3,4,5,10,15]) / 15
# xs.requires_grad_()
ys = (xs * 2 + 3 + torch.randn(8)) / 15
# ys.requires_grad_()

a = torch.randn(1,requires_grad=True)
b = torch.randn(1,requires_grad=True)
# y = m * x + b

def predict(x):
    return a * x + b


optim = SGD([a,b],lr=0.1)

training = True
real_loss = 1000
while real_loss > 0.02:
    optim.zero_grad()
    preds = predict(xs)
    mse = torch.mean((preds - ys) ** 2)
    mse.backward()
    print(mse.item())
    real_loss = mse.item()
    optim.step()

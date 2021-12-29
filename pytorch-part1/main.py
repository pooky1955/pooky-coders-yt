import torch
import matplotlib.pyplot as plt

xs = torch.Tensor([1,2,3,4,5,10,15]) 
ys = (2 * xs + 5 ) 

a = torch.randn(1)
b = torch.randn(1)

a.requires_grad_()
b.requires_grad_()

def predict(inputs):
    return a * inputs + b

def mse(answers,predicted):
    return torch.mean((answers - predicted) ** 2)



loss = 1000
while loss > 0.0000000001:
    predicted = predict(xs)
    mse_loss = mse(ys,predicted)
    print(f"loss : {mse_loss.item()}")
    mse_loss.backward()
    loss = mse_loss.item()

    with torch.no_grad():
        a = a - a.grad * 0.3
        b = b - b.grad * 0.3
    a.requires_grad_()
    b.requires_grad_()


preds = predict(xs)
plt.plot(xs.detach().cpu(),ys.detach().cpu(),label="actual answers")
plt.plot(xs.detach().cpu(),preds.detach().cpu(),label="predicted answers")
plt.legend()
plt.show()

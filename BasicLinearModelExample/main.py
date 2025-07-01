import torch
import torch.nn as nn

class LinearModel(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        self.linear_01 = nn.Linear(in_features=784, out_features=100)
        self.relu_01 = nn.ReLU()
        self.linear_02 = nn.Linear(in_features=100, out_features=num_classes)


    def forward(self,x):
        x = self.linear_01(x)
        x = self.relu_01(x)
        output = self.linear_02(x)
        return output

input_tensor = torch.randn(size=(64,784))
print(input_tensor.size())
linear_model = LinearModel(num_classes=10)

output_tensor = linear_model(input_tensor)
print(output_tensor.size())

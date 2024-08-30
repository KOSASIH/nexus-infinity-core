import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader

class NeuralNetwork(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(NeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim) 
        self.fc2 = nn.Linear(hidden_dim, hidden_dim) 
        self.fc3 = nn.Linear(hidden_dim, output_dim) 

    def forward(self, x):
        x = torch.relu(self.fc1(x)) 
        x = torch.relu(self.fc2(x)) 
        x = self.fc3(x) 
        return x

class ConvolutionalNeuralNetwork(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(ConvolutionalNeuralNetwork, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5) 
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5) 
        self.fc1 = nn.Linear(320, hidden_dim) 
        self.fc2 = nn.Linear(hidden_dim, output_dim) 

    def forward(self, x):
        x = torch.relu(self.conv1(x)) 
        x = torch.relu(self.conv2(x)) 
        x = x.view(-1, 320) 
        x = torch.relu(self.fc1(x)) 
        x = self.fc2(x) 
        return x

class RecurrentNeuralNetwork(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(RecurrentNeuralNetwork, self).__init__()
        self.rnn = nn.LSTM(input_dim, hidden_dim, num_layers=2, batch_first=True) 
        self.fc = nn.Linear(hidden_dim, output_dim) 

    def forward(self, x):
        h0 = torch.zeros(2, x.size(0), self.hidden_dim).to(device) 
        c0 = torch.zeros(2, x.size(0), self.hidden_dim).to(device) 
        out, _ = self.rnn(x, (h0, c0)) 
        out = self.fc(out[:, -1, :]) 
        return out

class NeuralNetworkEnsemble:
    def __init__(self, models):
        self.models = models

    def forward(self, x):
        outputs = []
        for model in self.models:
            output = model(x)
            outputs.append(output)
        return torch.stack(outputs).mean(dim=0)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# Example usage:
nn_model = NeuralNetwork(input_dim=100, hidden_dim=50, output_dim=10)
cnn_model = ConvolutionalNeuralNetwork(input_dim=100, hidden_dim=50, output_dim=10)
rnn_model = RecurrentNeuralNetwork(input_dim=100, hidden_dim=50, output_dim=10)
ensemble_model = NeuralNetworkEnsemble([nn_model, cnn_model, rnn_model])
input_data = np.random.rand(100, 100)  # Replace with your input data
output = ensemble_model(torch.tensor(input_data))
print(output.shape)

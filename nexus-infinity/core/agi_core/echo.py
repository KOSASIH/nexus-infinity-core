import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

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

class Echo:
    def __init__(self, input_dim, hidden_dim, output_dim, learning_rate, batch_size, epochs):
        self.nn = NeuralNetwork(input_dim, hidden_dim, output_dim)
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = optim.Adam(self.nn.parameters(), lr=learning_rate)
        self.batch_size = batch_size
        self.epochs = epochs
        self.scaler = StandardScaler()

    def process_input(self, input_data):
        # Preprocess input data
        input_data = self.scaler.fit_transform(input_data)

        # Create dataset and data loader
        dataset = EchoDataset(input_data)
        data_loader = DataLoader(dataset, batch_size=self.batch_size, shuffle=True)

        # Train neural network
        for epoch in range(self.epochs):
            for batch in data_loader:
                inputs, labels = batch
                inputs, labels = inputs.to(device), labels.to(device)
                self.optimizer.zero_grad()
                outputs = self.nn(inputs)
                loss = self.criterion(outputs, labels)
                loss.backward()
                self.optimizer.step()

        # Evaluate neural network
        outputs = self.nn(input_data)
        _, predicted = torch.max(outputs, 1)
        accuracy = accuracy_score(input_data, predicted)
        report = classification_report(input_data, predicted)
        matrix = confusion_matrix(input_data, predicted)

        return accuracy, report, matrix

class EchoDataset(Dataset):
    def __init__(self, input_data):
        self.input_data = input_data

    def __len__(self):
        return len(self.input_data)

    def __getitem__(self, idx):
        input_data = self.input_data[idx]
        label = input_data[-1]
        input_data = input_data[:-1]
        return torch.tensor(input_data), torch.tensor(label)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# Example usage:
echo = Echo(input_dim=100, hidden_dim=50, output_dim=10, learning_rate=0.001, batch_size=32, epochs=10)
input_data = np.random.rand(100, 100)  # Replace with your input data
accuracy, report, matrix = echo.process_input(input_data)
print("Accuracy:", accuracy)
print("Classification Report:\n", report)
print("Confusion Matrix:\n", matrix)

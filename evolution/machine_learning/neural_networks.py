import torch
import torch.nn as nn
import torch.optim as optim

class NeuralNetworks:
    def __init__(self, config):
        self.config = config
        self.model = self.create_model()

    def create_model(self):
        # Define a simple neural network architecture
        model = nn.Sequential(
            nn.Linear(self.config['input_dim'], self.config['hidden_dim']),
            nn.ReLU(),
            nn.Linear(self.config['hidden_dim'], self.config['output_dim'])
        )
        return model

    def evolve(self, population):
        # Train the neural network using the population as training data
        criterion = nn.MSELoss()
        optimizer = optim.Adam(self.model.parameters(), lr=self.config['learning_rate'])

        for individual in population:
            inputs, targets = individual
            optimizer.zero_grad()
            outputs = self.model(inputs)
            loss = criterion(outputs, targets)
            loss.backward()
            optimizer.step()

        return self.model

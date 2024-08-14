import torch
from torch.utils.data import DataLoader, TensorDataset
from models.lstm_model import LSTMModel
import numpy as np

# Dummy data for demonstration purposes
input_size = 3
sequence_length = 10
hidden_size = 50
num_layers = 2
output_size = 1

X_train = np.random.rand(100, sequence_length, input_size).astype(np.float32)
y_train = np.random.rand(100, output_size).astype(np.float32)

train_dataset = TensorDataset(torch.tensor(X_train), torch.tensor(y_train))
train_loader = DataLoader(dataset=train_dataset, batch_size=16, shuffle=True)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = LSTMModel(input_size, hidden_size, num_layers, output_size).to(device)
criterion = torch.nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Training loop
for epoch in range(10):
    for i, (inputs, targets) in enumerate(train_loader):
        inputs, targets = inputs.to(device), targets.to(device)
        
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if (i+1) % 10 == 0:
            print(f'Epoch [{epoch+1}/10], Step [{i+1}/{len(train_loader)}], Loss: {loss.item():.4f}')

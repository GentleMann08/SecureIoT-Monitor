import torch
from data_preprocessing import load_data, preprocess_data, create_sequences, split_data
from lstm_model import LSTMModel
from train_model import train_model, evaluate_model

def main():
    filepath = "data/iot_traffic.csv"
    seq_length = 50
    input_size = 10
    hidden_size = 50
    num_layers = 2
    output_size = 2
    num_epochs = 20
    batch_size = 32
    learning_rate = 0.001

    data = load_data(filepath)
    data_scaled, scaler = preprocess_data(data)
    X, y = create_sequences(data_scaled, seq_length)
    X_train, X_test, y_train, y_test = split_data(X, y)

    train_dataset = TensorDataset(torch.tensor(X_train, dtype=torch.float32), torch.tensor(y_train, dtype=torch.long))
    test_dataset = TensorDataset(torch.tensor(X_test, dtype=torch.float32), torch.tensor(y_test, dtype=torch.long))

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

    model = LSTMModel(input_size, hidden_size, num_layers, output_size).to(torch.device("cuda" if torch.cuda.is_available() else "cpu"))
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    model = train_model(model, train_loader, criterion, optimizer, num_epochs)
    accuracy = evaluate_model(model, test_loader)

    print(f"Model Accuracy: {accuracy:.4f}")

if __name__ == "__main__":
    main()
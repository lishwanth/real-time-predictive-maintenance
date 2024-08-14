import unittest
import torch
from models.lstm_model import LSTMModel

class TestLSTMModel(unittest.TestCase):
    def test_lstm_forward(self):
        model = LSTMModel(input_size=3, hidden_size=50, num_layers=2, output_size=1)
        test_input = torch.randn(1, 10, 3)
        output = model(test_input)
        self.assertEqual(output.shape, (1, 1))

if __name__ == "__main__":
    unittest.main()
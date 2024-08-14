import pandas as pd

class DataLoader:
    def load_data(self, file_path):
        df = pd.read_csv(file_path)
        return df

# Example Usage
if __name__ == "__main__":
    loader = DataLoader()
    data = loader.load_data("datasets/turbofan/train_FD001.txt")
    print(data.head())

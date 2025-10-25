import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


def prediction_function(data, target, test_size=0.2):
    """
    This function splits data for machine learning
    """

    x_train, x_test, y_train, y_test = train_test_split(
        data, target, test_size=test_size, random_state=42
    )

    print("Data shape:", data.shape)
    print(f"Training set size: {len(x_train)}")

    return x_train, x_test, y_train, y_test


class ModelPreprocessor:
    def __init__(self, data):
        self.data = data
        self.processed_data = None

    def clean_data(self):
        # Remove missing values
        self.processed_data = self.data.dropna()
        return self.processed_data

    def normalize_data(self):
        if self.processed_data is not None:
            # Normalize numeric columns
            numeric_columns = self.processed_data.select_dtypes(
                include=[np.number]
            ).columns
            self.processed_data[numeric_columns] = (
                self.processed_data[numeric_columns]
                - self.processed_data[numeric_columns].mean()
            ) / self.processed_data[numeric_columns].std()
        return self.processed_data


# Example usage
if __name__ == "__main__":
    # Create sample data
    data = pd.DataFrame(
        {
            "feature1": [1, 2, 3, 4, 5, None],
            "feature2": [2, 4, 6, 8, 10, 12],
            "target": [0, 1, 0, 1, 0, 1],
        }
    )

    # Initialize preprocessor
    preprocessor = ModelPreprocessor(data)

    # Clean and normalize
    clean_data = preprocessor.clean_data()
    normalized_data = preprocessor.normalize_data()

    print("Original data shape:", data.shape)
    print("Clean data shape:", clean_data.shape)
    print("Normalized data:\n", normalized_data.head())

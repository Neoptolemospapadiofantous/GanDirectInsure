from abc import ABC, abstractmethod


class IModel(ABC):

    @abstractmethod
    def save(self, file_path):
        """Save the model to the specified file path."""
        pass

    @abstractmethod
    def load(self, file_path):
        """Load the model from the specified file path."""
        pass

    @abstractmethod
    def train(self, data, labels):
        """Train the model on the provided data."""
        pass

    @abstractmethod
    def predict(self, data):
        """Predict using the model on the provided data."""
        pass

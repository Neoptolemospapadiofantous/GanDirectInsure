from abc import ABC, abstractmethod


class IAlgorithm(ABC):

    @abstractmethod
    def train(self, data, labels):
        """Train the algorithm on the provided data."""
        pass

    @abstractmethod
    def predict(self, data):
        """Predict using the algorithm on the provided data."""
        pass

    @abstractmethod
    def evaluate(self, data, labels):
        """Evaluate the algorithm's performance on the provided data."""
        pass

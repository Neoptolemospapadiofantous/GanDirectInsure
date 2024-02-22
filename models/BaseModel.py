from interfaces.i_model import IModel


class BaseModel(IModel):
    def save(self, file_path):
        # Implementation for saving the model
        pass

    def load(self, file_path):
        # Implementation for loading the model
        pass

    def train(self, data):
        # Implementation for training the model
        pass

    def predict(self, data):
        # Implementation for making predictions
        pass

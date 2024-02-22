from sklearn.ensemble import RandomForestClassifier
from models.base_model import BaseModel


class RandomForestModel(BaseModel):
    def __init__(self, n_estimators=100, random_state=42):
        self.model = RandomForestClassifier(
            n_estimators=n_estimators, random_state=random_state)

    def train(self, data, labels):
        self.model.fit(data, labels)

    def predict(self, data):
        return self.model.predict(data)

    def save(self, file_path):
        # Here, you would add logic to save the trained model to a file
        import joblib
        joblib.dump(self.model, file_path)

    def load(self, file_path):
        # Here, you would add logic to load the model from a file
        import joblib
        self.model = joblib.load(file_path)

from sklearn.ensemble import RandomForestClassifier
from interfaces.i_algorithm import IAlgorithm


class RandomForestAlgorithm(IAlgorithm):
    def __init__(self, n_estimators=100, max_depth=None, random_state=None):
        self.model = RandomForestClassifier(n_estimators=n_estimators,
                                            max_depth=max_depth,
                                            random_state=random_state)

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X):
        return self.model.predict(X)

    def evaluate(self, X_test, y_test):
        # Evaluate the model and return some performance metric. Here, we'll use accuracy.
        return self.model.score(X_test, y_test)

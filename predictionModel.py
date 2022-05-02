from joblib import load
from sklearn.metrics import r2_score

class Model():

    def __init__(self):
        self.model = load("assets/pipeline.joblib")

    def make_predictions(self, data):
        result = self.model.predict(data)
        return result

    def calcuate_r2(self, data_x, data_y):
        y_pred = self.model.predict(data_x)
        return r2_score(data_y, y_pred)


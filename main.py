from fastapi import FastAPI
from pydantic import BaseModel

import pandas as pd

from dataModel import DataModel, DataModelR2
from predictionModel import Model

model = Model()

app = FastAPI()

class ResultPrediction(BaseModel):
    Expectativa: float

class ResultR2(BaseModel):
    R2_Calculado: float

@app.get("/")
def read_root():
   return {"Hello": "World"}

@app.post("/predict", response_model=ResultPrediction)
def make_predictions(dataModel: DataModel ):
    df = pd.DataFrame(dataModel.dict(), columns=dataModel.dict().keys(), index=[0])
    df.columns = dataModel.columns()
    result = model.make_predictions(df)
    return {"Expectativa": result}

@app.post("/calculate_r2", response_model=ResultR2)
def make_predictions(dataModelR2: DataModelR2 ):
    x = []
    for i in range(len(dataModelR2.predictory)):
        x.append(dataModelR2.predictory[i].dict())
    df_x = pd.DataFrame(x)
    df_y = pd.DataFrame(dataModelR2.expected)
    result = model.calcuate_r2(df_x, df_y)
    return {"R2_Calculado": result}




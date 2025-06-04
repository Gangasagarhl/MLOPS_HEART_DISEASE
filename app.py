import sys
import os

import certifi
ca = certifi.where()

from dotenv import load_dotenv
load_dotenv()
mongo_db_url = os.getenv("MONGODB_URL_KEY")
print(mongo_db_url)
import pymongo
from heartdisease.exception.exception import HeartDiseaseException
from heartdisease.logging.logger import logging
from heartdisease.pipeline.training_pipeline import TrainingPipeline

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile,Request
from uvicorn import run as app_run
from fastapi.responses import Response
from starlette.responses import RedirectResponse
import pandas as pd

from heartdisease.utils.main_utils.utils import load_object

from heartdisease.utils.ml_utils.model.estimator import NetworkModel


client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

from heartdisease.constant.training_pipeline import DATA_INGESTION_COLLECTION_NAME
from heartdisease.constant.training_pipeline import DATA_INGESTION_DATABASE_NAME

database = client[DATA_INGESTION_DATABASE_NAME]
collection = database[DATA_INGESTION_COLLECTION_NAME]
import requests
app = FastAPI()
origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="./templates")

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train_route():
    try:
        train_pipeline=TrainingPipeline()
        train_pipeline.run_pipeline()
        return Response("Training is successful")
    except Exception as e:
        raise HeartDiseaseException(e,sys)
    


@app.get("/predict")
async def predict_form(request: Request):
    return templates.TemplateResponse("predict_form.html", {"request": request})

@app.post("/predict")
async def predict_route(
    request: Request,
    age: int = Form(...),
    sex: int = Form(...),
    cp: int = Form(...),
    trestbps: int = Form(...),
    chol: int = Form(...),
    fbs: int = Form(...),
    restecg: int = Form(...),
    thalach: int = Form(...),
    exang: int = Form(...),
    oldpeak: float = Form(...),
    slope: int = Form(...),
    ca: int = Form(...),
    thal: int = Form(...)
):
    try:
        # Create a DataFrame from form inputs
        data = {
            'age': [age],
            'sex': [sex],
            'cp': [cp],
            'trestbps': [trestbps],
            'chol': [chol],
            'fbs': [fbs],
            'restecg': [restecg],
            'thalach': [thalach],
            'exang': [exang],
            'oldpeak': [oldpeak],
            'slope': [slope],
            'ca': [ca],
            'thal': [thal]
        }
        df = pd.DataFrame(data)
        
        # Load preprocessor and model
        preprocessor = load_object("final_model/preprocessor.pkl")
        final_model = load_object("final_model/model.pkl")
        network_model = NetworkModel(preprocessor=preprocessor, model=final_model)
        
        # Make prediction
        y_pred = network_model.predict(df)
        prediction = y_pred[0]  # Assuming y_pred is a list or array
        
        # Determine message and class based on prediction
        if prediction == 0:
            message = "You are safe, but check with doctor."
            class_name = "safe"
        else:
            message = "Check with the doctor immediately."
            class_name = "warning"
        
        # Return result template
        return templates.TemplateResponse("result.html", {"request": request, "message": message, "class_name": class_name})
    
    except Exception as e:
        raise HeartDiseaseException(e, sys)
    
    
if __name__=="__main__":
    app_run(app,host="0.0.0.0",port=8080)

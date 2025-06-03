"""
Apache Airflow introduced the TaskFlow API which allows you to create tasks 
using Python decorators like @task. This is a cleaner and more intuitive way 
of writing tasks without needing to manually use operators like PythonOperator.
Let me show you how to modify the previous code to use the @task decorator.
"""

from airflow import DAG
from airflow.decorators import task
from datetime import datetime
from packages.Extract import Extract
from packages.Transform import Transform
from packages.Load import Load
import pandas as pd
import json


## Define the DAG

with DAG(
    dag_id='ETL_WITH_HEART_DISEASE',
    start_date=datetime(2025,6,3),
    schedule='@once',
    catchup=False,
) as dag:
    

    
    @task
    def extract():
        print("extracting the data from the location")
        obj = Extract(path="https://raw.githubusercontent.com/Gangasagarhl/MLOPS_HEART_DISEASE/refs/heads/main/heart.csv")
        print("Oject created")
        data:pd.DataFrame = obj.extract()
        print("extraction is done")
        return data
    
    
    @task
    def transform(data):
        print("Transformation started\n")
        obj =  Transform(data)
        conversion = obj.transform()
        print("conversion is done")
        return conversion
    
   
    @task
    def load(records):
        print("load has been started")
        
        DATABASE="heartdata"
        Collection="heartdatacollection"

        obj =Load()
        value =obj.insert_data_mongodb(records=records,database=DATABASE,collection =Collection)

        print("Number of records inserted is : ", value)

    
   
    
    ## Set task dependencies
    start_value=extract()
    data_changed=transform(start_value)
    load(data_changed)